console.log("siteCommon 1.5.8");

// Splide Client Loader
// Place the Splide Options in the data-splide attibute
// Example: <div class="splide" data-splide='{"type":"loop","perPage":3}'></div>

if (typeof Splide === "function" && typeof loadSplide === "function") {
  loadSplide();
} else {
  const carousels = document.getElementsByClassName("splide");
  if (carousels.length > 0 && !window.location.href.includes("/c/sponsored")) {
    for (let i = 0; i < carousels.length; i++) {
      new Splide(carousels[i]).mount();
    }
  }
}

//Glideco Client Loader

typeof prepTrack === "function"
  ? prepTrack()
  : console.log("Glideco not loaded or not found in DOM");

//Link wrapper v.1.0
console.log("Link Wrapper v.1.0");

(() => {
  console.log("====== Link Wrapper 1.0 ======");
  const wrapInLinks = document.querySelectorAll(".link-wrap");

  //Link Wrapper -- querySelectorAll(".link-wrap");
  wrapInLinks?.length > 0 &&
    wrapInLinks?.forEach((card) => {
      card.addEventListener("click", (ev) => {
        ev.stopPropagation();
        card.querySelector(".main-link")?.click();
      });
    });
})();

//Featured Tiles v1.3
function loadFeaturedTilesWide() {
  console.log("Featured Tiles v.1.3");
  function isFlexWrapping(ul) {
    const containerWidth = ul.clientWidth;
    let childrenWidth = 0;
    for (const child of ul.children) {
      childrenWidth += child.offsetWidth;
    }
    return childrenWidth > containerWidth;
  }

  function isShowMoreButton(ulEl, button) {
    if (isFlexWrapping(ulEl)) {
      button.style.display = "flex";
    } else {
      button.style.display = "none";
    }
  }

  function resizeListener(content, showAllButton) {
    if (isFlexWrapping(content)) {
      showAllButton.style.display = "flex";
      if (content.dataset.expanded === "true") {
        content.style.maxHeight = content.scrollHeight + "px";
        showAllButton.innerHTML = "Show less";
      } else {
        content.style.maxHeight = null;
        showAllButton.innerHTML = "Show All";
      }
    } else {
      showAllButton.style.display = "none";
      content.style.maxHeight = null;
      content.dataset.expanded = "false";
      showAllButton.innerHTML = "Show All";
    }
  }

  const contentWrap = document.querySelectorAll(".quicktile__wrap");

  contentWrap.forEach((content) => {
    if (typeof content.dataset.expanded === "undefined") {
      content.dataset.expanded = "false";
    }

    const buttonParent = content.parentElement;
    const preexistingButton = buttonParent.querySelector(".show-all");

    if (preexistingButton) {
      preexistingButton.remove();
    }

    const showAllButton = document.createElement("div");
    showAllButton.classList.add("show-all");
    showAllButton.innerHTML =
      content.dataset.expanded === "true" ? "Show less" : "Show All";
    content.parentNode.insertBefore(showAllButton, content.nextSibling);

    if (content.dataset.expanded === "true") {
      const prevTransition = content.style.transition;
      content.style.transition = "none";
      content.style.maxHeight = content.scrollHeight + "px";
      void content.offsetHeight;
      content.style.transition = prevTransition || "";
      showAllButton.innerHTML = "Show less";
    } else {
      content.style.maxHeight = null;
      showAllButton.innerHTML = "Show All";
    }

    window.removeEventListener("resize", resizeListener);
    window.addEventListener("resize", () => {
      resizeListener(content, showAllButton);
    });

    showAllButton.addEventListener("click", function () {
      if (content.dataset.expanded === "true") {
        content.style.maxHeight = null;
        showAllButton.innerHTML = "Show All";
        content.dataset.expanded = "false";
      } else {
        content.style.maxHeight = content.scrollHeight + "px";
        showAllButton.innerHTML = "Show less";
        content.dataset.expanded = "true";
      }
    });
    isShowMoreButton(content, showAllButton);
  });
}
loadFeaturedTilesWide();

// SEO Hide/Show toggle
//button comes from espot JS and should be removed.
if (typeof showMoreButton === "undefined" && typeof button === "undefined") {
  let showMoreButton = document.querySelector(".toggle-button");
  let showMoreHiddenItems = document.querySelectorAll(".hidden-item");
  let isShowMoreHidden = true;
  showMoreButton?.addEventListener("click", () => {
    showMoreButton.textContent = isShowMoreHidden ? "Show Less" : "Show More";
    isShowMoreHidden = !isShowMoreHidden;
    showMoreHiddenItems.forEach((item) => item.classList.toggle("hidden"));
  });
}

//Petco Promo Scheduler
//v.2.5.0
console.log("Promo Scheduler v.2.5.0");
// 1. Add  data-scheduled-promos ATTRIBUTE to PARENT ELEMENT where the value matches the the CONST name of the promo schedule object. ie:
//  data-scheduled-promos="EDLPSchedule"
// 2. Add .scheduled class to tile
// 3. Add data-promo-id="{promoName}" to tile
// 4. Add the .scheduled CSS rule to styles
// .scheduled { display: none !important;}
// .scheduled.active { display: flex !important; }
// 5. Update the `OBJNAME` matching the data-promo-id with the object.
// 6. create a script tag with the date object
/*
  <script>
  const EDLPSchedule ={
  PROMOID1: {
    activeDates: [
      {
        startDate: new Date("06/30/2024"),
        endDate: new Date("07/04/2024 23:59:59"),
      },
    ],
  },

  defaultDate: "05/30/2024",
}
</script>
*/
// 6. Update the defaultDateString to the date you'd like to display if nothing else is scheduled.
if (typeof promoScheduler === "undefined") {
  promoScheduler = {
    promos: {},

    add: function (json) {
      this.promos = { ...this.promos, ...json };
      return this;
    },

    get: function () {
      return this.promos;
    },

    isCurrentlyActive: function (promo, date) {
      let currentDate = date;
      const promoId = promo.dataset.promoId;
      let result = false;
      if (this.get()[promo.dataset.promoId]) {
        this.get()[promoId].activeDates.forEach((dateRange) => {
          if (
            currentDate >= dateRange.startDate &&
            currentDate <= dateRange.endDate
          ) {
            result = true;
          }
        });
      }
      return result;
    },

    run: (date = new Date(), isFound = false) => {
      const scheduledSpots = [...document.querySelectorAll(".scheduled")];
      let foundActiveSchedule = isFound;
      for (const promo of scheduledSpots) {
        if (promoScheduler.isCurrentlyActive(promo, new Date(date))) {
          promo.classList.add("active");
          foundActiveSchedule = true;
        } else {
          promo.classList.remove("active");
        }
      }
      if (!foundActiveSchedule && promoScheduler.get().defaultDate) {
        promoScheduler.run(promoScheduler.get().defaultDate, true);
      }
    },
  };

  function promodate(date) {
    const picker = document.createElement("input");
    picker.type = "date";
    picker.id = "promo-date-picker";
    picker.style.cssText =
      "position:fixed;bottom:50vh;left:50px;background:white;";
    picker.valueAsDate = new Date();

    picker.addEventListener("change", (e) => {
      promoScheduler.run(e.target.value.replace("-", "/"));
    });
    document.body.appendChild(picker);
    window.addEventListener("keyup", (e) => {
      if (document.querySelector("#promo-date-picker") && e.key === "Escape") {
        document.body.removeChild(picker);
      }
    });
  }

  window.addEventListener("keydown", (e) => {
    //Ctrl-Shift-D opens up date picker for QA
    if (
      e.ctrlKey &&
      e.shiftKey &&
      e.keyCode === 68 &&
      !document.querySelector("#promo-date-picker")
    ) {
      promodate();
    }
  });
}

document.querySelectorAll("[data-scheduled-promos]").forEach((promo) => {
  promoScheduler.add(eval(`${promo.dataset.scheduledPromos}`)).run();
});

// Quicktile Carousel v.1.2.0
console.log("Quicktile Carousel v.1.2.0");
let quicktileContainer = document.querySelector(".quicktile-wrap");
let quicktileContent = document.querySelectorAll(".quicktile:not(.hidden)");
let quicktileControl = document.querySelectorAll(".quicktile-carousel-cntrl");
let controls = quicktileContainer
  ? quicktileContainer.parentElement.parentElement.querySelector(".controls")
  : null;

if (
  typeof quicktileContainer !== "undefined" &&
  typeof quicktileContent !== "undefined" &&
  typeof quicktileControl !== "undefined"
) {
  setFirstItem();
  setLastItem();
  quicktileShowHideArrows();
}

document.addEventListener("click", delegate(toggleFilter, toggleHandler));

function delegate(criteria, listener) {
  let el = undefined;
  return function (e) {
    el = e.target;
    do {
      if (!criteria(el)) {
        continue;
      }
      e.delegateTarget = el;
      listener.call(this, e);
      return;
    } while ((el = el.parentNode));
  };
}

function setFirstItem() {
  const firstTile = quicktileContent[0];
  if (firstTile) {
    firstTile.classList.add("first-item");
  }
}

function setLastItem() {
  const lastTile = quicktileContent[quicktileContent.length - 1];
  if (lastTile) {
    lastTile.classList.add("last-item");
  }
}

function quicktileShowHideArrows() {
  const activeTilesCount = quicktileContent.length;
  if (controls) {
    if (activeTilesCount <= 4) {
      controls.style.display = "none";
    } else {
      controls.style.display = "block";
    }
  }
}

function toggleFilter(elem) {
  return (
    elem instanceof HTMLElement && elem.matches(".quicktile-carousel-cntrl")
  );
}

function toggleHandler(e) {
  const el = document.querySelector(".last-item");
  const currSliderControl = e.delegateTarget;
  el.classList.remove("last-item");

  let newSeat;
  if (currSliderControl.getAttribute("data-toggle") === "next") {
    newSeat = next(el);
    quicktileContainer.classList.remove("is-reversing");
  } else {
    newSeat = prev(el);
    quicktileContainer.classList.add("is-reversing");
  }

  newSeat.classList.add("last-item");
  newSeat.style.order = 1;
  for (let i = 2; i <= quicktileContent.length; i++) {
    newSeat = next(newSeat);
    newSeat.style.order = i;
  }
  quicktileContainer.classList.remove("first-item");
  setTimeout(function () {
    quicktileContainer.classList.add("first-item");
  }, 150);

  function next(el) {
    if (el.nextElementSibling) {
      return el.nextElementSibling.classList.contains("hidden")
        ? next(el.nextElementSibling)
        : el.nextElementSibling;
    } else {
      return quicktileContainer.firstElementChild.classList.contains("hidden")
        ? next(quicktileContainer.firstElementChild)
        : quicktileContainer.firstElementChild;
    }
  }

  function prev(el) {
    if (el.previousElementSibling) {
      return el.previousElementSibling.classList.contains("hidden")
        ? prev(el.previousElementSibling)
        : el.previousElementSibling;
    } else {
      return quicktileContainer.lastElementChild.classList.contains("hidden")
        ? prev(quicktileContainer.lastElementChild)
        : quicktileContainer.lastElementChild;
    }
  }
}

/*Tabco v.1.2.0
  Usage:
  1. Give your tabs a role="tab" and the parent element a data-tabco-id="some-id"
  2. Give your tabs a data-panel that matches the #3 👇
  3. Give your carousel__track a data-panel that matches #2 👆
*/

const tabButtons = [
  ...document.querySelectorAll('[data-tabco-id] [role="tab"]'),
];
const tabPanels = [...document.querySelectorAll(".tab-panel")];

let showHideTracks = (tab, tabButtons) => {
  tabButtons.map((tabButton) => {
    tabButton.classList.remove("active");
    tabButton.setAttribute("aria-selected", "false");
  });

  tabPanels.map((panel) => {
    panel.classList.remove("active");
    if (panel.id === tab.dataset.panel) {
      panel.classList.add("active");
      tab.classList.add("active");
      tab.setAttribute("aria-selected", "true");
    }
  });
};

tabButtons.forEach((tab) => {
  tab.addEventListener("click", (e) => {
    showHideTracks(tab, tabButtons);
  });
});

//Personalization to add a name to content from the cookie.
// let nameSpan = document.querySelector('.first-name');
// let firstName = `${document.cookie
//   ?.split(';')
//   .find((cookie) => cookie.trim().startsWith('pfirstname'))
//   ?.split('=')[1]
//   .replace('%20', ' ')}, `;
// if (nameSpan && firstName && firstName.match(/^\w*,/gi)) {
//   nameSpan.style.display = 'inline';
//   nameSpan.innerHTML = firstName;
//   nameSpan.nextSibling.textContent =
//     nameSpan.nextSibling?.textContent[0]?.toLowerCase() + nameSpan.nextSibling?.textContent?.slice(1);
// } else {
//   console.log("No name found...");
// }

function loadModalco() {
  console.log("Modalco v1.5.5");

  const openModal_Buttons = document.querySelectorAll(".modal__open-btn");
  const closeModal_Buttons = document.querySelectorAll(".modal__close-btn");

  const focusableElements = [
    "button",
    "[href]",
    "input",
    "select",
    "textarea",
    '[tabindex]:not([tabindex="-1"])',
  ];

  const closeModals = (ev) => {
    ev.preventDefault();
    document.querySelectorAll(".modalco").forEach((modal) => {
      modal.classList.remove("modal__open");
      modal.parentElement.classList.remove("active");
    });
    //Restore normal page scroll behaviour
    document.body.style.overflowY = "visible";
  };

  // Open modal functionality

  const handleOpenModal = (ev) => {
    ev.preventDefault();
    closeModals(ev);
    const modalTarget = ev.target.dataset.modalTarget;
    console.log(modalTarget);
    if (modalTarget) {
      const modal = document.querySelector(`[data-modal="${modalTarget}"]`);
      const backdrop = modal.parentElement;
      if (modal) {
        modal.classList.add("modal__open");
        // Prevent page scroll when modal is open
        document.body.style.overflowY = "hidden";
        backdrop.classList.add("active");

        if (backdrop) {
          backdrop.addEventListener("click", (e) => {
            e.preventDefault();
            closeModals(ev);
          });
        }
      }
    }
  };

  openModal_Buttons.forEach((btn) => {
    btn.removeEventListener("click", handleOpenModal);
    btn.addEventListener("click", handleOpenModal);
  });

  closeModal_Buttons.forEach((btn) =>
    btn.addEventListener("click", (ev) => {
      document.body.style.overflowY = "";
      ev.preventDefault();
      closeModals(ev);
    })
  );

  window.addEventListener("keyup", (ev) => {
    ev.keyCode === 27 ? closeModals(ev) : null;
  });

  const firstFocusableElement = document.querySelectorAll(focusableElements)[0];
  const focusableContent = document.querySelectorAll(focusableElements);
  const lastFocusableElement = focusableContent[focusableContent.length - 1];
  document.addEventListener("keydown", function (e) {
    let isTabPressed = e.key === "Tab" || e.keyCode === 9;
    if (!isTabPressed) {
      return;
    }

    if (e.shiftKey) {
      // if shift key pressed for shift + tab combination
      if (document.activeElement === firstFocusableElement) {
        lastFocusableElement.focus(); // add focus for the last focusable element
        e.preventDefault();
      }
    } else {
      // if tab key is pressed
      if (document.activeElement === lastFocusableElement) {
        // if focused has reached to last focusable element then focus first focusable element after pressing tab
        firstFocusableElement.focus(); // add focus for the first focusable element
        e.preventDefault();
      }
    }
  });
}

loadModalco();

// FAQs v.1.0.0
var faqAccordion = document.querySelectorAll(".site-faqs dt");
var i;

for (i = 0; i < faqAccordion.length; i++) {
  faqAccordion[i].onclick = function () {
    var faq = this.nextElementSibling;
    var faqPanel = document.querySelectorAll(".site-faqs dd");
    var faqPanelActive = document.querySelectorAll(".site-faqs dt");

    if (faq.style.maxHeight) {
      faq.style.maxHeight = null;
      this.classList.remove("active");
    } else {
      for (var ii = 0; ii < faqPanelActive.length; ii++) {
        faqPanelActive[ii].classList.remove("active");
      }
      for (var iii = 0; iii < faqPanel.length; iii++) {
        this.classList.remove("active");
        faqPanel[iii].style.maxHeight = null;
      }
      faq.style.maxHeight = faq.scrollHeight + "px";
      this.classList.add("active");
    }
  };
}
