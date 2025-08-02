const $rmn = (function () {
  const rmnAds = [];
  const url = { impression_url: '', click_url: '', network_ip: '' };
  const events = [];

  const RMN_SESSION_ID = 'RMN_SESSION_ID';

  const getSessionId = () => {
    const sessionCookie = getCookie('rmn_session_id');
    const sessionJson = window.localStorage.getItem(RMN_SESSION_ID);

    let session;

    if (sessionCookie) {
      const sessionCookieArray = sessionCookie.split('|');
      const [sessionId, sessionExpiry] = sessionCookieArray;
      window.localStorage.setItem(
        RMN_SESSION_ID,
        JSON.stringify({ id: sessionId, expiry: sessionExpiry })
      );
      session = JSON.stringify({ id: sessionId, expiry: sessionExpiry });
    }

    if (!session && sessionJson) {
      session = JSON.parse(sessionJson);
    }

    return session;
  };

  function impressionCall(element) {
    const dataRmnAdTag = element?.getAttribute('data-rmn-ad-tag');
    const dataRmnAdRequestId = element?.getAttribute('data-rmn-ad-request-id');
    const dataRmnAdItemId = element?.getAttribute('data-rmn-ad-item-id');
    const dataRmnCreativeId = element?.getAttribute('data-rmn-creative-id');
    const dataRmnAdSource = element?.getAttribute('data-rmn-ad-source');
    const session = getSessionId();
    const sessionId = session && JSON.parse(session)?.id;
    const sessionExpiry = session && JSON.parse(session)?.expiry;

    events.push({
      event: 'impression',
      dataRmnAdTag,
      adRequestId: dataRmnAdRequestId,
      time: new Date().toISOString(),
    });

    const payload = {
      adTag: dataRmnAdTag,
      adRequestId: dataRmnAdRequestId,
      adItemId: dataRmnAdItemId,
      creativeId: dataRmnCreativeId,
      cache: dataRmnAdSource === 'site-served' ? true : false,
      customerId: getCookie('WC_UserId') ?? '-1002',
      displayedAt: new Date().toISOString(),
      payload: { sessionId, sessionExpiry },
    };

    if (!dataRmnAdItemId) {
      console.log('[ERROR] rmn impression fields are missing', payload);
      return;
    }
    fetch(url.impression_url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Session-Id': sessionId,
        'X-Customer-Id': getCookie('WC_UserId') ?? '-1002',
        'X-Guest-Id': sessionId,
        'X-WCS-Id': getCookie('WC_UserId') ?? '-1002',
        'X-User-Type':
          getCookie('WC_UserType') === 'R' ? 'registered' : 'guest',
        'X-Forwarded-For': url.network_ip ?? '',
      },
      body: JSON.stringify({ ...payload }),
    }).catch((error) =>
      console.log('[ERROR] fetch rmn impression call', error)
    );
  }

  function getCookie(cookieName) {
    const cookieValue = document.cookie
      .split('; ')
      .find((cookie) => cookie.startsWith(`${cookieName}=`));

    return cookieValue ? cookieValue.split('=')[1] : null;
  }

  function clickEvent(event) {
    const element = event?.currentTarget;
    const dataRmnAdTag = element?.getAttribute('data-rmn-ad-tag');
    const dataRmnAdRequestId = element?.getAttribute('data-rmn-ad-request-id');
    const dataRmnAdItemId = element?.getAttribute('data-rmn-ad-item-id');
    const dataRmnCreativeId = element?.getAttribute('data-rmn-creative-id');
    const dataRmnAdSource = element?.getAttribute('data-rmn-ad-source');
    const session = getSessionId();
    const sessionId = session && JSON.parse(session)?.id;
    const sessionExpiry = session && JSON.parse(session)?.expiry;

    const impressionTime = events.find(
      ({ adRequestId, event }) =>
        event === 'impression' && adRequestId === dataRmnAdRequestId
    )?.time;

    events.push({
      event: 'click',
      dataRmnAdTag,
      adRequestId: dataRmnAdRequestId,
      time: new Date().toISOString(),
    });

    const payload = {
      adTag: dataRmnAdTag,
      adRequestId: dataRmnAdRequestId,
      adItemId: dataRmnAdItemId,
      creativeId: dataRmnCreativeId,
      cache: dataRmnAdSource === 'site-served' ? true : false,
      customerId: getCookie('WC_UserId') ?? '-1002',
      clickedAt: new Date().toISOString(),
      displayedAt: impressionTime,
      payload: { sessionId, sessionExpiry },
    };
    if (!impressionTime || !dataRmnAdItemId) {
      console.log('[ERROR] rmn click impressionTime field is missing', payload);
      return;
    }
    fetch(url.click_url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-Session-Id': sessionId,
        'X-Customer-Id': getCookie('WC_UserId') ?? '-1002',
        'X-Guest-Id': sessionId,
        'X-WCS-Id': getCookie('WC_UserId') ?? '-1002',
        'X-User-Type':
          getCookie('WC_UserType') === 'R' ? 'registered' : 'guest',
        'X-Forwarded-For': url.network_ip ?? '',
      },
      keepalive: true,
      body: JSON.stringify({ ...payload }),
    }).catch((error) => console.log('[ERROR] fetch rmn click call', error));
  }

  function bindRMNEvents() {
    rmnAds?.forEach((banner) => {
      const options = { root: null, rootMargin: '0px', threshold: 0.5 };

      const handleIntersection = (entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            const dataRmnAdRequestId = entries?.[0]?.target?.getAttribute(
              'data-rmn-ad-request-id'
            );
            const isImpressionCallFired = events.some(
              ({ adRequestId, event }) =>
                event === 'impression' && adRequestId === dataRmnAdRequestId
            );
            if (!isImpressionCallFired) {
              impressionCall(entries?.[0]?.target);
            }
          }
        });
      };

      const observer = new IntersectionObserver(handleIntersection, options);
      observer.observe(banner);

      banner?.addEventListener('click', clickEvent);
    });
  }

  function init({ impression_url, click_url, network_ip }) {
    if (!impression_url || !click_url) {
      console.log('please pass url properly');
      return null;
    }

    url.impression_url = impression_url;
    url.click_url = click_url;
    url.network_ip = network_ip;
    const rmnAdElements = document.querySelectorAll('[data-ad-source="rmn"]');

    // Removing old events.
    rmnAds?.forEach((banner) => {
      banner.removeEventListener('click', clickEvent);
    });
    rmnAds.length = 0; // Deleting all elements of the array

    rmnAds.push(...rmnAdElements);
    bindRMNEvents();
  }

  return { init, url, rmnAds, events };
})();

window.$rmn = $rmn;
