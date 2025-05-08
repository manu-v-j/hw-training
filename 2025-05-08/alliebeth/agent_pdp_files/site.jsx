

	if (window.attachEvent){
		window.attachEvent('onload', checkJQuery);
	}else{
		window.addEventListener('load', checkJQuery);
	}
	var clientID = 0;
	var leadSurvey;
	var lrSurveyCookie;

	function checkJQuery(){
		if(!window.jQuery)
		{
		   var script = document.createElement('script');
		   script.type = "text/javascript";
		   script.src = "https://ajax.googleapis.com/ajax/libs/jquery/1.8.3/jquery.min.js";
		   document.getElementsByTagName('head')[0].appendChild(script);
		}
	}

	function checkValidate(){
		if(window.jQuery)
		{
		   var script = document.createElement('script');
		   script.type = "text/javascript";
		   script.src = "https://ajax.aspnetcdn.com/ajax/jquery.validate/1.11.1/jquery.validate.min.js";
		   document.getElementsById('agentContent').validate(script);
		}
	}

	function isRequiredField(form){
		for(var i=0; i<form.elements.length;i++){
			if(form.elements[i].value == ''){
				alert("This field is required!");
				form.elements[i].focus();
				return false;
			}
		} return true;
	}

	jQuery(document).on('focus click', '.expand input', function(e){
        $(this).parent().addClass('expanded');
    });

    jQuery(document).on('blur', '.expand input', function(e){
        $(this).parent().removeClass('expanded');
    });

	function submitFormAgentContent(form){
		if (isRequiredField(form)) {
			form.submit();
		}
	}

	function isValidDateFormat(date){
    		return date.match(/^(?:\d{1,2}([\./-])\d{1,2}\1(?:\d{4}|\d{2})|(?:(?:jan(?:uary)?)|(?:feb(?:ruary)?)|(?:mar(?:ch)?)|(?:apr(?:il)?)|(?:may)|(?:jun(?:e)?)|(?:jul(?:y)?)|(?:aug(?:ust)?)|(?:sept?(?:tember)?)|(?:oct(?:ober)?)|(?:nov(?:ember)?)|(?:dec(?:ember)?))\.?\s+\d{1,2},?\s+\d{4})$/i) != null;
	 }

	function isValidEmailFormat(email){
		return email.match(/[^\.][a-z0-9\._\%\-]*@(?:[a-z0-9\-]+\.)+([a-z]{2,4}|museum|travel)$/i) != null;
		//return email.match(/^[_a-zA-Z0-9-]+(\.[_a-zA-Z0-9-]+)*(\+[a-zA-Z0-9-]+)*@[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*\.(([0-9]{1,3})|([a-zA-Z]{2,3})|(aero|coop|info|museum|name))$/) != null;
	 }

	function isValidPhoneFormat(phone){
		phone = phone.replace(/[^\d]/g, '');
		return phone.match(/^(?:1?(\d{3}))?(\d{3})(\d{4})(\d*)$/) != null;
	 }

	 function getClientID(){
		 if (clientID == 0 && document.cookie.match(/(?:sessionclientid=|sessionclientid=.+?&clientid=)(\d+)/i))
			clientID = RegExp.$1;

		return clientID;
	 }

	function clearClientID() {
		try{
			var date = new Date();
			date.setTime(date.getTime() + (-1 * 864e5));
			document.cookie = 'sessionclientid=; expires=' + date.toGMTString() + '; path=/'; document.cookie = 'client=; expires=' + date.toGMTString() + '; path=/';
		}
		catch(ex){}
	}

	/* Encodes a URL the way a server would. The javascript method encodeURI() misses some characters. */
	function urlEncode(string) {
		var encodedString = string;
		var chars = [['\\:', '3a'], ['\\.', '2e'], ['\\/', '2f'], ['\\?', '3f'], ['\\=', '3d'], ['\\&', '26'], ['\\+', '2b'], ['\\^', '5e'], ['\\|', '7c'], ['\\>', '3e'], ['\\<', '3c'], ['\\~', '7e'], ['\\[', '5b'], ['\\]', '5d'], ['\\$', '24'], ['\\,', '2c'], ['\\s', '20'], ['\\#', '23'], ['\'', '27']];
		for (var i = 0; i < chars.length; i++) {
			var exp = new RegExp(chars[i][0], 'gi');
			exp = chars[i][0];
			encodedString = eval('encodedString.replace(/' + exp + '/gi, \'%\' + chars[i][1])');
		}
		return encodedString;
	}


	function showWebOverlay(responseOrOpts, closeBtn){
		if (typeof(responseOrOpts) != "string") {
			var opts = responseOrOpts || {};
			response = opts.response;
			closeBtn = opts.closeBtn;
			bgOpacity = opts.bgOpacity;
			ldp = opts.ldp;
		}
		else {
			response = responseOrOpts;
			bgOpacity = 0.6;
			ldp = false;
		}

		/*try closing overlay in the event that link was inadvertantly clicked multiple times.*/
		if($('#overlayParent').length > 0) {
			removeWebOverlay(closeBtn);
	    }

        var body = $('body');

        var content = $('<div id="overlayParent"/>').css({
            position:'absolute',
            background:'#ffffff',
            zIndex:1001
        }).append(response).appendTo(body);

        var contentWidth = content.outerWidth(true);
        var contentHeight = content.outerHeight(true);

        var documentWidth = $(document).width();
        var documentHeight = $(document).height();

        var windowWidth = $(window).width();
        var windowHeight = $(window).height();

        var widthOffset = window.pageXOffset ? window.pageXOffset : (document.documentElement || document.body.parentNode || document.body).scrollLeft;
        var heightOffset = window.pageYOffset ? window.pageYOffset : (document.documentElement || document.body.parentNode || document.body).scrollTop;

        var contentPositionLeft = ((windowWidth - contentWidth) / 2) + widthOffset;
        var contentPositionTop = ((windowHeight - contentHeight) / 2) + heightOffset;

        if (contentPositionLeft < 0) {
            contentPositionLeft = 0;
        }

        if (contentPositionTop < 0) {
            contentPositionTop = 0;
        }

		content.css('left', contentPositionLeft + 'px');
		content.css('top', contentPositionTop + 'px');

        $('<div id="overlayMask"/>').css({
            position: 'fixed',
            top: 0,
            left: 0,
            width: documentWidth + 'px',
            height: documentHeight + 'px',
            background: '#000000',
            opacity: bgOpacity,
            zIndex: 1000
        }).appendTo(body);

		// Do not generate a close button if there's already a close button (id="aClose") on the form
		if(closeBtn && response.indexOf("id=\"aClose\"") == -1) {
            var close = $('<div id="overlayClose"><a href="javascript:void(0);"></a></div>').css({ position: 'absolute', right: '2px', top: '5px', zIndex: 1001, nowrap: 'nowrap', width: '50px', height: '16px', cursor: 'pointer' }).click(ldp ? null : removeWebOverlay);
			content.append(close);
		}
    }

	function removeWebOverlay(closeBtn){
		$("#overlayParent").remove();
        $("#overlayMask").remove();
        $('#overlayParentWrapper').remove();

		if(closeBtn) {
			$("#overlayClose").remove();
        }

        if (typeof(CloseOverlay) == "function") {
            CloseOverlay();
        }

        if (typeof(CloseLDPOverlay) == "function") {
            CloseLDPOverlay();
        }

		// Hide an additional overlay
		if (typeof amplify === "object") {
			var hideOnClose = amplify.store("hideOnClose");
			if (hideOnClose !== undefined) {
				amplify.store("hideOnClose", null);
				$(hideOnClose).hide();
			}
		}
	}

	function removeFormLRE(closeBtn){
		$("#overlayParent").remove();
		$("#overlayMask").remove();

		if(closeBtn) {
			$("#overlayClose").remove();
		}

		if(leadSurvey.length > 0) {
			doneLeadingRE(leadSurvey);
		}
	}

	function doneLeadingRE(survey){
		if(survey.length > 0 ){
				var loc = "http://www.leadingre.com/" + survey + "?COID=10206";
				window.open(loc,'_blank');
		}
	}

	/* resize overlay mask and center overlay on window resize. */
	$(function(){
		$(window).resize(function(){
			var windowHeight = $(window).height();
			var windowWidth = $(window).width();

			var overlayTop =  (windowHeight  - $('#overlayParent').height())/2;
			var overlayLeft = (windowWidth - $('#overlayParent').width())/2;

			if(overlayTop < 0)
				overlayTop = 10;

			if(overlayLeft < 0)
				overlayLeft = 10;

			$('#overlayMask').css({ height:$(document).height(), width:$(document).width() }).show();
			$('#overlayParent').css({ top: overlayTop, left: overlayLeft}).show();
		}).resize();
	});


	function getQsParam(name) {
		name = name.replace(/[\[]/, "\\\[").replace(/[\]]/, "\\\]");
		var regexS = "[\\?&]" + name + "=([^&#]*)";
		var regex = new RegExp(regexS);
		var results = regex.exec(window.location.search);
		if(results == null)
			return "";
		else
			return decodeURIComponent(results[1].replace(/\+/g, " "));
	}

    function saveListing(opts) {
		clientID = getClientID();
		if(clientID > 0) {
			opts.clientID = clientID;
			saveFavoriteOverlay(opts);
		}
		else
			getLoginPage(opts);
	}

	function getSoldData(opts){
		clientID = getClientID();

		if(clientID > 0) {
		 /* do nothing */
		} else {
			getLoginPage(opts);
		}

	}

	function throwWarning(message){
		if (typeof(console)=='object' && typeof(console.warn)=='function')
			console.warn(message);
	}

	function getLoginPage(selectedOrOpts, goto, mlsid, mlsnumber, fxn, sender, subDetail, extraData){
		var noRefresh = false;
		var bgo = 0.6;
		if (typeof(selectedOrOpts) != "string"){
			var opts = selectedOrOpts||{};
			selected = opts.selected;
			/*properties = opts.properties;*/
			goto = opts.goto;
			mlsid = opts.mlsID;
			mlsnumber = opts.mlsNumber;
			fxn = opts.callback;
			sender = opts.sender;
			subDetail = opts.subDetail;
			extraData = opts.extraData;
			title = opts.extranetTitle;
			noRefresh = opts.noRefresh;
			favoriteAction = opts.favoriteAction;
			bgOpacity = opts.bgOpacity || bgo;
			closeBtn = opts.closeBtn || false;
			ldp = opts.ldp;
		} else {
			throwWarning('Pass an object to getLoginPage instead of argument list')
			selected = selectedOrOpts;
			title= ''; /*may need to change this to retrieve extranet title */
			favoriteAction = undefined;
			bgOpacity = bgo;
			closeBtn = false;
			ldp = false;
		}

		clearClientID();
		if (selected == 'clientlogout') {
			$.ajax({ url: '/abaag/modules/internet/extranet/myextranet.asp', data:'selected=' + selected + '&overlay=true', dataType: 'html', success:getLogoutCallback, error: getLogoutFail});
		} else {
			var url = '/abaag/modules/internet/extranet/myextranet.asp';
			var data = 'selected=' + selected + '&overlay=true&et=' + title;

			if (goto && !favoriteAction) {
				url = '/abaag/modules/internet/extranet/listingportal.asp';
				data = 'detail=' + goto + '&overlay=true';
			}

			if(mlsid)
				data += '&mlsid=' + mlsid;

			if(mlsnumber)
				data += '&mlsnumber=' + mlsnumber;

			if(noRefresh)
				data += '&noRefresh=' + noRefresh;

			if(fxn)
				data += '&selected=' + selected + '&fxn=' + fxn;

			if(sender)
				data += '&sender=' + sender;

			if(subDetail)
				data += '&subDetail=' + subDetail;

			if(bgOpacity)
				data += '&bgOpacity=' + bgOpacity;

            if(extraData)
                data += '&' + extraData;

			if(favoriteAction)
				data += '&favAction=' + favoriteAction;

			$.ajax({ url: url, data: data, dataType: 'html', success:function(xml){getLoginPageCallback({response:xml, closeBtn: closeBtn, ldp: ldp, bgOpacity:bgOpacity});}, error: getLoginPageFail});
		}
	}

	function getLogoutCallback() {
		document.location.replace(document.location.href)

		 /* Note: this is the overlay.xslt version; extranetOverlay-js.asp was using document.location.reload(); */
	}

	function getLogoutFail(response) {
		alert('There was an error logging you out.  Please refresh window and try again.');
	}

	function scrubHtml(html) {
		var htmlFixedJscomments = html.replace(/([^https?:]|^)\/\/(?!\s*-->)(.*)?[\r\n]/g, '$1/* $2 */');
		var htmlNoWhiteSpace = htmlFixedJscomments.replace(/(?:[\r\n\t]+|\s{2,})/g,'');
		return htmlNoWhiteSpace;
	}

	function getLoginPageCallback(responseOrOpts){
		if (typeof(responseOrOpts) != "string"){
			var opts = responseOrOpts||{};
			response = opts.response;
			bgOpacity = opts.bgOpacity;
			closeBtn = opts.closeBtn;
			ldp = opts.ldp;
		} else {
			response = responseOrOpts;
			bgOpacity = 0.6;
			closeBtn = false;
			ldp = false;
		}

		var text = scrubHtml(response);
		showWebOverlay({response:text, closeBtn:closeBtn, ldp: ldp, bgOpacity:bgOpacity});
	}

	function getLoginPageFail(response){
		alert('There was an error logging you in.  Please refresh window and try again.');
	}

	function removeFormOverlay() {
		removeWebOverlay();
	}

	function removePageOverlay() {
		removeWebOverlay();
	}

	function openPrivacyWindow (URL) {
		aWindow=window.open (URL, "Privacy", "toolbar=no,width=300,height=300,status=no,scrollbars=no,resizable=yes,menubar=no");
	}



	/*/Added on 12-15-14 for Lead Capture form for Leading RE(JLS)*/
	function getLeadCaptureForm(companyid,frm,evnt){
		leadSurvey = evnt;
		lrSurveyCookie = getformCookie("lrePassed");

		if(lrSurveyCookie != null && lrSurveyCookie == "yes"){
			doneLeadingRE(leadSurvey);
		}
		else if(frm!=null && frm.length > 0 && companyid > 0){
			getOverlayForm(companyid,frm,'','');

		}
	}

	function getformCookie(name){
		if(name.length > 0){
			var temp;
			var strCookies = document.cookie.split(';');
			for(var i = 0; i < strCookies.length; i ++){
				var c = strCookies[i];
				if(c.indexOf(name) != -1)
					temp = c.substring(c.indexOf("=") +1)
			}
		}
		return temp;
	}

	/*/Added on 11-1-14 for Home Values Lead forms*/
	function getLeadForm(companyid,formName){
		var compid;
		if(companyid > 0){
			compid = companyid;
		}
		else{
			var strCookies = document.cookie.split(';');
			for(var i = 0; i < strCookies.length; i ++){
				var c = strCookies[i];
				if(c.indexOf("rncoid") != -1)
					compid = c.substring(c.indexOf("=") +1)
			}
		}
		if(compid > 0 && formName.length > 0){
			getOverlayForm(compid, formName, '', '');
		}
	}
	function getCalloutFormOverlay(evnt, url, name, newWindow){
	/*Needed to create additional function that calls getOverlayForm due to what the callout config files pass*/
		var companyid = 697;
		var formtype = url.substr(0, url.lastIndexOf("."));
		getOverlayForm(companyid, formtype, '', '');
	}

	/*/JM: Added getOverlayForm function on 10-1-12 for overlay forms*/
	function getOverlayForm(companyid, formtype, mlsid, mlsnumber){
		var data = ['f=' + formtype, 'comp=' + companyid, 'mlsid=' + mlsid, 'sitedirectory=abaag', 'mlsnumber=' + mlsnumber, 'overlay=true', 'acc=656495'];

		if (isSearchForm({formName: formtype.toLowerCase()}))
			data.push('issearchform=true');
		if(leadSurvey != null){
			data.push('frmtrack=true');
			if(leadSurvey == "national"){
					data.push('form=reloNationalH');
			}
			else if(leadSurvey == "searchworld"){
					data.push('form=reloInternationalH');
			}
		}


		$.ajax({ url: '/abaag/modules/internet/forms/form.aspx', data:data.join('&'), dataType: 'json', success:getFormCallback, error: getFormFail, complete: checkTranslations});
	}

	function getForm(mlsid, mlsnumber, companyid, isOverlay){ /*I believe 318 uses this function - JM */
		$.ajax({ url: '/abaag/modules/internet/forms/form.aspx', data:'f=ListingInformationRequest&issearchform=true&comp=' + companyid + '&mlsid=' + mlsid + '&mlsnumber=' + mlsnumber + (isOverlay ? '&overlay=true' : ''), dataType: 'json', success:getFormCallback, error: getFormFail});
	}

	function getFormCallback(response){
		showWebOverlay(scrubHtml(response.html), true);
		$('#divForm input').focus();
	}

    function checkTranslations() {
        if (document.cookie.match(/culture\=\w+/i) != null
            && document.cookie.match(/culture\=\w+/)[0].indexOf('fr') > 0) {
            if ($('#schedule-showing-overlay').length > 0) {
                var formOverlay = {
                    overlay: $('#schedule-showing-overlay'),
                    firstName: $('#schedule-showing-overlay').find('#firstName'),
                    lastName: $('#schedule-showing-overlay').find('#lastName'),
                    email: $('#schedule-showing-overlay').find('#emailAddress'),
                    phone: $('#schedule-showing-overlay').find('#phone1'),
                    message: $('#schedule-showing-overlay').find('textarea[name="notes"]'),
                    submit: $('#schedule-showing-overlay').find('#schedule-showing-overlay-container-form-submit'),
                    header: $('#schedule-showing-overlay').find('h2').eq(0)
                }

                formOverlay.firstName[0].placeholder = "Prénom";
                formOverlay.lastName[0].placeholder = "Nom de famille";
                formOverlay.email[0].placeholder = "Courriel";
                formOverlay.phone[0].placeholder = "Téléphone";
                formOverlay.message[0].innerText = "Je souhaite faire une visite";
                formOverlay.submit[0].innerText = "Soumettre";
                formOverlay.header[0].innerText = "Programmer une projection";
                formOverlay.overlay.find('p').eq(0)[0].innerText = $('#schedule-showing-overlay').find('p').eq(0)[0].innerText.replace('MLS:', 'SIA:');
            }
        }
    }

	function getFormFail(response){
		alert('There was an error loading this form.  Please refresh window and try again.');

		/*Note: formOverlay.xslt had the function as "getFormFail(response, evnt, url, name, newWindow)"*/
	}

	/* 318 uses this function */
    function saveFavorite(mlsid, mlsnumber, clientid, closeFxn) {
		$.ajax({ url: '/abaag/modules/internet/extranet/savefavorite.asp', data:'overlay=true&fxn=' + closeFxn + '&clientid=' + clientid + '&mlsid=' + mlsid + '&mlsnumber=' + mlsnumber, dataType: 'html', success:saveFavoriteCallback, error: saveFavoriteFail});
	}


	function saveSearch(opts){
		clientID = getClientID();

		if(clientID > 0) {
			opts.clientID = clientID;
			saveSearchOverlay(opts);
		}
		else {
			saveSearchLogin(opts);
		}
	}

	function saveSearchLogin(opts){
		/* needed for login for recentsearches */
		var accountID = opts.accountid;
		var p = opts.p;
		var acc = opts.acc > 0 ? opts.acc : 0;
		var page = opts.page;
		var search = opts.search;
		var goto = opts.detail;
		var selected = opts.selected;
		var criteria = opts.criteria;
		var noRefresh = opts.noRefresh;
		var advanced = opts.advanced;
		var mlsID = opts.mlsid;
		var mlsName = opts.mlsname;

		var url = '';
		var data = p + '&selected=' + selected + '&overlay=true';

		if(accountID > 0) /* accountID present when p=microsite */
			data+= '&accountid=' + accountID;

        if(acc > 0)
		    data += '&acc=' + acc;

		data += '&page=' + page;
		data += '&search=' + search;
		data += '&criteria=' + criteria;
		data += '&noRefresh=' + noRefresh;

		if(advanced)
			data += advanced;

		if (goto) {
				url = '/abaag/modules/internet/extranet/listingportal.asp';
				data += '&detail=' + goto;
		}

		if (url.length + data.length > 2083)
			alert('The amount of criteria selected exceeds the limit for saved searches.\nPlease remove at least one criteria selection to save this search.');
		else
			$.ajax({ url: url, data: data, dataType: 'html', success: getLoginPageCallback, error: getLoginPageFail});
	}

	function saveSearchOverlay(opts){
		var accountID = opts.accountid;
		var p = opts.p;
		var acc = opts.acc > 0? opts.acc : 0;
		var page = opts.page;
		var search = opts.search;
		var goto = opts.detail;
		var selected = opts.selected;
		var criteria = opts.criteria;
		var noRefresh = opts.noRefresh;
		var advanced = opts.advanced;
		var mlsID = opts.mlsid;
		var mlsName = opts.mlsname;



		var data = p + '&selected=' + selected + '&overlay=true';

		if(accountID > 0) /* accountID present when p=microsite */
			data+= '&accountid=' + accountID;

		data += '&acc=' + acc;
		data += '&page=' + page;
		data += '&search=' + search;
		data += '&noRefresh=' + noRefresh;
		data += '&criteria=' + criteria;

		if(advanced)
			data += advanced;

		var url='/abaag/modules/internet/extranet/savesearch.asp';

		if (url.length + data.length > 2083)
			alert('The amount of criteria selected exceeds the limit for saved searches.\nPlease remove at least one criteria selection to save this search.');
		else
			$.ajax({ url: url, data: data, dataType: 'html', success:saveSearchCallback, error: saveSearchFail});
	}

	function saveSearchCallback(response){
		showWebOverlay(scrubHtml(response));
	}

	function saveSearchFail() {
		alert('failed');
	}

	function doneSaveSearchCallback(response) {
		if (response.substring((response.length - 21), response.length) == '^^savesearchsuccess^^') {
			var messageText = 'This search has been added to your saved searches.';
			var messageHtml = '<div width="400" style="padding:25px; font-weight:bold; text-align:center; background-color: white;">' + messageText + '<br/><br/><a href="javascript:void(0);" onclick="javascript:removeWebOverlay();">Continue</a></div>';
			showWebOverlay(messageHtml, true);
		} else {
			alert(response);
		}
	}

	function doneSaveSearchFail(response) {
		alert('There was an error saving this search to your saved searches.  Please refresh window and try again.');
	}

	function NeighborhoodTracker(opts, searchid, searchname) {
		clientID = getClientID();

		if(clientID > 0) {
			opts.clientID = clientID;
			NeighborhoodTrackerOverlay(opts, searchid, clientID, searchname);
		}
		else {
			NeighborhoodTrackerLogin("neighborhoodtracker", searchid, searchname);
		}
	}

	function NeighborhoodTrackerOverlay(opts, searchid, clientID, searchDescr){

		var data = 'searchid=' + searchid + '&clientid=' + clientID + '&searchname=' + searchDescr + '&overlay=true';

		var url='/abaag/modules/internet/extranet/neighborhoodtracker.aspx';

		$.ajax({ url: url, data: data, dataType: 'html', success:saveNeighborhoodCallback, error: saveSearchFail});
	}

	function saveNeighborhoodCallback(response, close){
		showWebOverlay(scrubHtml(response));
	}

	function NeighborhoodTrackerLogin(opts, searchid, searchname){
		/* needed for login for recentsearches */
		var accountID = opts.accountid;
		var p = opts.p;
		var acc = opts.acc > 0? opts.acc : 0;
		var page = opts.page;
		var search = opts.search;
		var goto = "neighborhoodtracker";
		var selected = opts.selected;

		var noRefresh = opts.noRefresh;
		var advanced = opts.advanced;
		var mlsID = opts.mlsid;
		var mlsName = opts.mlsname;

		var url = '/abaag/modules/internet/extranet/listingportal.asp';
		var data = 'detail=neighborhoodtracker&overlay=true&searchid=' + searchid + '&fxn=true&searchname=' + searchname;

		if (url.length + data.length > 2083)
			alert('The amount of criteria selected exceeds the limit for saved searches.\nPlease remove at least one criteria selection to save this search.');
		else
			$.ajax({ url: url, data: data, dataType: 'html', success: getNeighTrackerCallback, error: getLoginPageFail});
	}

	function getNeighTrackerCallback(responseOrOpts, close){
		if (typeof(responseOrOpts) != "string"){
			var opts = responseOrOpts||{};
			response = opts.response;
			bgOpacity = opts.bgOpacity;
			closeBtn = opts.closeBtn;
		} else {
			response = responseOrOpts;
			bgOpacity = 0.6;
			closeBtn = false;
		}

		var text = scrubHtml(response);
		showWebOverlay(text);
	}

	function saveFavoriteOverlay(mlsidOrOpts, mlsnumber, clientid, closeFxn){
		var noRefresh = false;
		if (typeof(mlsidOrOpts) != "number"){
			var opts = mlsidOrOpts||{};
			properties = opts.properties;
			mlsid = opts.mlsID;
			mlsnumber = opts.mlsNumber;
			clientid = opts.clientID;
			closeFxn = opts.callback;
			noRefresh = opts.noRefresh;
			favoriteAction = opts.favoriteAction;
		} else {
			mlsid = mlsidOrOpts;
			favoriteAction = undefined;

			if(closeFxn)
				noRefresh = false;
		}

		data = 'overlay=true&clientid=' + clientid;

		if(mlsid)
			data += '&mlsid=' + mlsid + '&mlsnumber=' + mlsnumber;

		if(closeFxn)
		data += '&fxn=' + closeFxn;

		if(noRefresh)
		data += '&noRefresh=' + noRefresh;

		if(favoriteAction)
			data += '&favAction=' + favoriteAction;

		var favPage;
		var favError;
		var favSuccess;
		if(favoriteAction && favoriteAction == 'savelikedlist') {
			favPage = 'favoriteshandler.aspx';
			favSuccess = saveLikedListSuccess;
			favError = saveLikedListError;
		} else {
			favPage = 'savefavorite.asp';
			favSuccess = saveFavoriteCallback;
			favError = saveFavoriteFail;
		}

		$.ajax({ url: '/abaag/modules/internet/extranet/' + favPage, data: data, dataType: 'html', success: favSuccess, error: favError });
	}

	function saveLikedListSuccess(response){
		removeWebOverlay();
		var search2 = $(Search);
		search2.trigger('removelikedlist');
	}

	function saveLikedListError(response){
		alert('There was an error saving list to your favorites');
	}

	function saveFavoriteCallback(response) {
		showWebOverlay(scrubHtml(response));
	}

	function saveFavoriteFail() {
		alert('There was an error saving this listing.  Please refresh window and try again.');
	}

	
	function isSearchForm(opts){
		opts = opts ||{}
		var formName = (opts.formName || '').toLowerCase();
		switch (formName) {
			case 'listinginformationrequest':
			case 'listingappointmentrequest':
			case 'consumerrequest_mortgage':
			case 'consumerrequest':
				return true;

			default:
				return false;
		}
	}


	/*I believe 318 uses this function - JM */
	function submitForm(form, formname, accid, mlsnumalpha, mlsid, price, city, clientid, submitbutton){
		if (validSubmissionOverlay(formname, form)) {
			if(submitbutton)
				submitbutton.disabled = true;

			if (typeof form != "undefined") // SN: 96978 - checked undefined condtion
			{
				var formdata = [];
				var qsdata = 'f='+formname+'&comp=697&acc='+accid+'&mlsnumber='+mlsnumalpha+'&mlsid='+mlsid+'&pr='+price+'&ct='+city+'&cid='+clientid;

				for (var i=0;i<form.elements.length;i++){
					if ((form.elements[i].type == 'checkbox' || form.elements[i].type == 'radio') && !form.elements[i].checked)
						continue;

					formdata.push(form.elements[i].name + '=' + encodeURIComponent(form.elements[i].value));
				}

				if (isSearchForm({formName:formname.toLowerCase()}))
					formdata.push('issearchform=true');

				$.ajax({ url: '/abaag/modules/internet/forms/form.aspx?' + qsdata, type: 'POST', data:formdata.join('&'), dataType: 'html', contentType: "application/x-www-form-urlencoded;charset=UTF-8", success:submitOverlayComplete, error: submitOverlayFail});
			}
		}
	}

    function submitFormOverlay(form, formname, accid, clientid, submitbutton, mlsnumalpha, mlsid, price, city, successCallback, errorCallback) {
        if (!successCallback) {
            successCallback = submitOverlayComplete;
        }

        if (!errorCallback) {
            errorCallback = submitOverlayFail;
        }

		var checkForDuplicateEmail = document.getElementById('checkForDuplicateEmailSchedule');


		if (checkForDuplicateEmail != null && checkForDuplicateEmail.value.length !== 0) {
            errorCallback();
			return false;
		}

        if (validSubmissionOverlay(formname, form)) {


            if (submitbutton)
                submitbutton.disabled = true;

            var formdata = [];
            var qsdata = 'f=' + formname + '&comp=697&tacc=' + accid + '&acc=' + accid + '&cid=' + clientid + '&overlay=true';

            if (mlsid != undefined) {
                qsdata += '&mlsnumber=' + mlsnumalpha + '&mlsid=' + mlsid + '&pr=' + price + '&ct=' + city;
            }

            if (formname.toLowerCase() == 'leadcapturere') {
                if (form.elements["fullName"] != null && form.elements["fullName"].value.length > 0) {
                    var _name = form.elements["fullName"].value.split(" ");
                    if (_name.length > 1) {
                        form.elements["firstName"].value = _name[0];
                        form.elements["lastName"].value = _name[1];
                    }
                }
                if (leadSurvey != null) {
                    if (leadSurvey == "national") {
                        qsdata += '&form=reloNationalHS&frmtrack=true';
                        formdata.push('form=reloNationalHS');
                    }
                    else if (leadSurvey == "searchworld") {
                        qsdata += '&form=reloInternationalHS&frmtrack=true';
                        formdata.push('form=reloInternationalHS');
                    }
                }
            }
            for (var i = 0; i < form.elements.length; i++) {
                if ((form.elements[i].type == 'checkbox' || form.elements[i].type == 'radio') && !form.elements[i].checked) {
                    continue;
                }

                formdata.push(form.elements[i].name + '=' + encodeURIComponent($(form.elements[i]).val())); /*extranetOverlay-js.asp used "form.elements[i].value" */
            }

            if (isSearchForm({ formName: formname.toLowerCase() }))
                formdata.push('issearchform=true');

            if (typeof (fbPixel) != 'undefined') {
                fbPixel.mlsnumber = mlsnumalpha;
                if (typeof (price) != 'undefined') { // SN: 117073
                    fbPixel.price = price.replace(new RegExp(/[^\.\d]+/g), '') + (new RegExp(/\.\d{2,}/).test(price) ? '' : '.00')
                }
            }

            $.ajax({ 
				url: '/abaag/modules/internet/forms/form.aspx?' + qsdata, 
				type: 'POST', 
				data: formdata.join('&'), 
				dataType: 'html', 
				contentType: "application/x-www-form-urlencoded;charset=UTF-8",
				success: successCallback, 
				error: errorCallback });
        }
        else {
            errorCallback();
        }
	}

	function submitSuccess(){
		removeWebOverlay();
		var messageHtml;
		var messageText;

		messageText = '<span class="overlayThanks">Thank you! Your message has been sent.</span>';
		messageHtml = '<div width="400" style="padding:20px; text-align:center; background-color: white;">' + messageText + '<br/><br/><a href="javascript:void(0);" onclick="javascript:removeWebOverlay();location.reload();">Continue</a></div>';
		showWebOverlay(messageHtml, true);

	}

    function submitOverlayComplete(response) {
		if(response == 'GetToKnowUs_OurServices' || response == 'SellersNeighborhoodSpecialist' || response == 'MeetYourClosingTeam' || response == 'InvestorSpecialist' || response == 'BuyersNeighborhoodSpecialist' || response == 'RelocationExpert'){
			submitSuccess();
		} else {
		removeWebOverlay();
		var messageHtml;
		var messageText;
		var responseJson = {};

		try { responseJson = eval('(' + response + ')'); } catch(ex) {}

		if (isNaN(response) && typeof(responseJson.adTracking) === 'undefined') {
			messageText = this.responseText;
			messageHtml = scrubHtml(messageText);
		}else{
			messageText = '<span class="overlayThanks">Thank you! Your message has been sent.</span>';
			if(leadSurvey != null){
				if(leadSurvey.length > 0){
					messageHtml = '<div width="400" style="padding:25px; font-weight:bold; text-align:center; background-color: white;">' + messageText + '<br/><br/><a href="javascript:void(0);" onclick="javascript:removeFormLRE();">Continue</a></div>';
				}
			}
			else{
				messageHtml = '<div width="400" style="padding:25px; font-weight:bold; text-align:center; background-color: white;">' + messageText + '<br/><br/><a href="javascript:void(0);" onclick="javascript:removeWebOverlay();">Continue</a></div>';
			}
			if(leadSurvey == null){
				if (responseJson.adTracking)
					messageHtml += scrubHtml(responseJson.adTracking);
			}

            if (responseJson.form && typeof(dataLayer) !== 'undefined') {
                switch (responseJson.form.toLowerCase()) {
                    case 'listingappointmentrequest':
                        dataLayer.push({ 'event': 'RNEvent', 'RNEventCategory': 'Form Submit Success', 'RNEventAction': 'Listing Appointment Request' });
                        break;
                    case 'listinginformationrequest':
                        dataLayer.push({ 'event': 'RNEvent', 'RNEventCategory': 'Form Submit Success', 'RNEventAction': 'Listing Information Request' });
                        break;
                }
            }
		}

		showWebOverlay(messageHtml, true);
        }

        // SN: 117073
        if (typeof (responseJson) != 'undefined' && typeof (responseJson.form) != 'undefined' &&
             (responseJson.form.toLowerCase() == 'listingappointmentrequest' || responseJson.form.toLowerCase() == 'listinginformationrequest'))
        {
            var type = responseJson.form.toLowerCase() == 'listingappointmentrequest' ? "Viewing Request" : "Information Request";
        }
	}

	function submitOverlayFail(response){
		alert('There was an error submitting this form.');
	}

	function validSubmissionOverlay(formname, frm) {
		formname = (typeof formname === "undefined") ? "" : formname; // SN: 96978
		var emailaddress;
		var firstName;
		var lastName;
		var phoneNumber;
		var phoneNumberRequired = "false" == 'true';
		var termsReadRequired = "false" == 'true';
	if(frm)	{
		emailAddress = frm.elements['emailAddress'];
		firstName = frm.elements['firstName'];
		lastName = frm.elements['lastName'];
		phoneNumber = frm.elements['phone1'];
		readTerms = frm.elements['termsverification'];
		remarks = frm.elements['notes'];
		fullName = frm.elements['fullName'];
        cityInterest = frm.elements['cityInterest'];
	} else {
		emailAddress = document.getElementById('emailAddress');
		firstName = document.getElementById('firstName');
		lastName = document.getElementById('lastName');
		phoneNumber = document.getElementById('phone1');
		readTerms = document.getElementById('termsverification');
		remarks = document.getElementById('notes');
		fullName = document.getElementById('fullName');
	}

		if (formname == 'ListingAppointmentRequest') {
			var apptDate;
			var apptTime;
			var todayDate = new Date();
			var mm = todayDate.getMonth();
			var dd = todayDate.getDate();
			var yy = todayDate.getFullYear();
			var companyid = 697;

			var tempDate = new Date(yy,mm,dd);
			var tempApptDate;

			if (frm)
			{
				apptDate = frm.elements['apptDate1'];
				apptTime = frm.elements['apptTime1'];
			}
			else
			{
				apptDate = document.getElementById('apptDate1');
				apptTime = document.getElementById('apptTime1');
			}

			if (apptDate && apptDate.value != null && apptDate.value != "") {
				if(apptDate.value.length < 10 || !isValidDateFormat(apptDate.value)) {
					alert("Please enter a valid date in the format: mm/dd/yyyy");
					apptDate.focus();
					return false;
				}
				else {
					tempApptDate = new Date(apptDate.value);

					if(companyid == 327){
						if (tempApptDate < tempDate) {
							alert("Request time can not be a past date");
							apptDate.focus();
							return false;
						}
					}
					else{
						if (tempApptDate <= tempDate) {
							alert("Please enter a future time");
							apptDate.focus();
							return false;
						}
					}

					if (apptTime.value.length == 0)
					{
						alert("Please enter an appointment time");
						apptTime.focus();
						return false;
					}
				}
			}
		}

		if(formname.toLowerCase() == 'leadcapturere'){
			if(fullName.value.trim() == "" || fullName.value.trim() == fullName.placeholder.trim()){
				alert("Please enter your first and last name.");
				fullName.focus();
				return false;
			}
			else if(fullName.value.indexOf(" ") < 0){
				alert("Please enter both first and last name");
				fullName.focus();
				return false;
			}
		}
		else{
			if (firstName != null) // SN: 96978 - checked NULL condition
			{
				if (firstName.value.trim() == "" || firstName.value.trim() == firstName.placeholder.trim()) {
					alert("Please enter your First Name.");
					firstName.focus();
					return false;
				}
			}
			if (lastName != null) // SN: 96978 - checked NULL condition
			{
				if (lastName.value.trim() == "" || lastName.value.trim() == lastName.placeholder.trim()) {
					alert("Please enter your Last Name.");
					lastName.focus();
					return false;
				}
			}
		}

		if (emailAddress != null) // SN: 96978 - checked NULL condition
		{
			if (!isValidEmailFormat(emailAddress.value)) {
				alert('Please enter a valid Email Address.');
				emailAddress.focus(); /* note: formOverlay.xslt had "emailAddress.select();" */
				return false;
			}else if (emailAddress.value.indexOf('@aol.com') != -1) {
				if (!confirm('AOL has known issues consistently delivering website system emails.\nUsing an alternate email address is highly recommended.\n\nClick OK to continue signup with an AOL email address.  Click Cancel to change email address.')){
					emailAddress.select();
					return false;
				}
			}
		}

		if (phoneNumber != null) { // SN: 96978 - checked NULL condition
			if(phoneNumber.value.length == 0 && phoneNumberRequired){
				alert('Please enter your Phone Number.');
				phoneNumber.focus();
				return false;
			} else if (!isValidPhoneFormat(phoneNumber.value) && phoneNumberRequired) {
				alert('Please enter a valid Phone Number.');
				phoneNumber.focus();
				return false;
			}
		}

         if(formname.toLowerCase() == 'homepartnersofamerica') {
            if (cityInterest){
                if(cityInterest.value.length == 0) {
                    alert('Please enter a City/Area You\'re Interested In.');
                    cityInterest.focus();
				    return false;
                }
            }
        }

		if (termsReadRequired) {
			if ((typeof readTerms != "undefined") && !readTerms.checked ) { // SN: 96978 - checked NULL condition
				alert('You must agree with the Terms of Use before continuing.');
				return false;
			}
		}

		if(formname == 'LendersReport' || formname == 'HomeValuesReport'){
			if (remarks.value.trim() == "" || remarks.value.trim() == 'Remarks') {
				alert("Please enter your notes.");
				remarks.focus();
				return false;
			}
		}

		return true;
	}

	function reloadPage(senderOrOpts) {
		/* refresh parent page...
		Used for SRP and LDPs.*/
		if(window.opener) {
			try {
				window.opener.location = window.opener.location.href.replace(/&(point|mode)=[^&]+/,'');
			} catch (ex){
				try{
					window.opener.location.reload(false);
				 } catch(ex){}
			}
		}

		/* refresh popup */
		var currentLocation = new String(document.location);
		/*some pages are putting a ? mark after '&mode=N', causing error. */
		var newLocation = currentLocation.replace('&mode=N?', '').replace('&mode=N', '');

		if(senderOrOpts){
			if (typeof(senderOrOpts) != "string"){
				var opts = senderOrOpts||{};
				sender = opts.sender;
				noRefresh = opts.noRefresh;


				if(!sender && noRefresh) {
					removeWebOverlay();
				}
			}
			else {
				sender = senderOrOpts;
			}

			if(sender) {
				newLocation = newLocation.replace('&mode=done', '');
				/*if there's a sender value, pass value as form parameter - would be a link/button id*/
				var form = $('<form action="' + newLocation + '" method="post"><input type="hidden" name="sender" value="' + sender + '" /></form>');
				$('body').append(form);
				$(form).submit();
			}
		}
		else
			document.location.href = newLocation;
	}

	/* This is for inline client login, now utilized on LDP */
	function tryLdpInlineLogin(username, rememberMe, password, passwordRequired, fxn, mlsID, mlsNumber, useOverlays){
			clearClientID();
			var usernameField = $('input[name=' + username + ']');
			var passwordField = $('input[name=' + password + ']');
			var qsPwd = '';

			var usernameValue = $.trim(usernameField.val());
			var passwordValue = $.trim(passwordField.val());

			if (usernameValue.length == 0) {
				alert('Please enter your email address.');
				usernameField.focus();
				return false;
			}

			/* ensure email format*/
			if (passwordRequired && passwordValue.length == 0) {
				alert('Please enter your password.');
				passwordField.focus();
				return false;
			}

			if (passwordValue.length > 0 ) {
				qsPwd = '&password=' + passwordValue;
			}

			$('input[name=username]').val(usernameValue);
			$('input[name=password]').val(passwordValue);

			var qsdata = 'detail=ldpClientLogin&mode=done&mlsid=' + mlsID + '&mlsnumber=' + mlsNumber + '&fxn=' + fxn;
			if(useOverlays){
				qsdata+='&overlay=true';
				var url = '/abaag/modules/internet/extranet/listingportal.asp?' + qsdata;
				$.ajax({ url: '/abaag/modules/internet/extranet/listingportal.asp?' + qsdata, type: 'POST', data:'username=' + usernameValue + qsPwd, dataType: 'html', success:doneLdpLoginCallback, error: doneLdpLoginFail});
			}
			else {
				var formAction ='/abaag/modules/internet/extranet/listingportal.asp?' + qsdata;
				var form = $('<form action="' + formAction + '" method="post"><input type="hidden" name="username" value="' + usernameValue + '" /><input type="hidden" name="password" value="' + passwordValue + '" /><input type="hidden" name="remember" value="" /></form>');
				form.action = formAction;
				$('body').append(form);
				$(form).submit();
			}

		return false;
	}

	function doneLdpLoginFail(response) {
		alert('FAIL:\n' + response);
	}

	function doneLdpLoginCallback (response) {
		if (response.substring((response.length - 16), response.length) == '^^loginsuccess^^') {
			document.location.reload();
		} else {
			var text = scrubHtml(response);
			showWebOverlay(text);
		}
	}

	/*unsure if this function is being used*/
	function doneLLoginFail(response) {
		alert('fail: \n' + response);
	}

	function focused(node) {
		node = $(node);
		var parent = node.parent();
		var child = $(parent.children('div')[0]);
		child.attr('oc',child.css('color')).css({visibility:'hidden'});
		node.css({color:'#000', backgroundColor:'#fff'})
	}

	function blured(node) {
		node = $(node);
		var parent = node.parent();
		var child = $(parent.children('div')[0]);
		if($.trim(node.val()).length > 0)
			child.attr('oc',child.css('color')).css({visibility:'hidden'});
		else
			child.attr('oc',child.css('color')).css({visibility:'visible'});
	node.css({color:child.attr('oc'), backgroundColor:'transparent'});
	}

	function getMarketWatchOverlay(companyID, distance, mlsID, lat, lng, clientID) {
		var data = 'companyid=' + companyID + '&distance=' + distance + '&mlsid=' + mlsID + '&lat=' + lat + '&lng=' + lng + '&save=true&clientid=' + clientID;
		$.ajax({ url: '/abaag/modules/internet/marketReport.aspx', data: data, dataType: 'html', success: getMarketWatchOverlayCallback, error: getMarketWatchOverlayFail });
	}

	function getMarketWatchOverlayCallback(response) {
		showWebOverlay(scrubHtml(response));
	}

	function getMarketWatchOverlayFail() {
		alert('There was an error with your request.  Please refresh window and try again.');
	}

	/*JM: Added 4-2-14 for cross-browser placeholder support. */
	function hideFieldPlaceholder(pInput) {
		var input = $(pInput);
        if (input.val() == '' || input.val() == input.attr('placeholder')) {
			input.addClass('placeholder');
			input.val(input.attr('placeholder'));
		}
	}

    function showFieldPlaceholder(pinput) {
		var input = $(pinput);
		if (input.val() == input.attr('placeholder')) {
			input.val('');
			input.removeClass('placeholder');
		}
    }

	function clearPlaceholdersOnSubmit(form){
		$(form).find('[placeholder]').each(function () {
			var input = $(this);
			if (input.val() == input.attr('placeholder')) {
				input.val('');
			}
		});
	}

    /**
     * WPTL-2025 Facebook Event Tracking
     */
    var fbPixel = {
        hasPixel: function () {
            return typeof (fbq) != 'undefined';
        }
        , track: function (event, data) {
            if (this.hasPixel() == false) return;

            var custom = arguments[2] || false;
            fbq(custom ? 'trackCustom' : 'track', event, data);
            if (fbPixel['mlsnumber']) delete fbPixel.mlsnumber;
            if (fbPixel['price']) delete fbPixel.price;
        }
        , trackFromElementEvent: function (event, data, elemObj) {
            if (this.hasPixel() == false) return;

            var custom = arguments[3] || false;
            data = data || elemObj.data;
            elemObj.elem.on(elemObj.jQEvent, elemObj.callback, { event: event, data: data, triggerElem: elemObj.elem });
        }
};

var monthNameByIndex = ["January",
                        "February",
                        "March",
                        "April",
                        "May",
                        "June",
                        "July",
                        "August",
                        "September",
                        "October",
                        "November",
                        "December"];
var monthAbbrByIndex = ["JanuaryAbbreviated",
                        "FebruaryAbbreviated",
                        "MarchAbbreviated",
                        "AprilAbbreviated",
                        "MayAbbreviated",
                        "JuneAbbreviated",
                        "JulyAbbreviated",
                        "AugustAbbreviated",
                        "SeptemberAbbreviated",
                        "OctoberAbbreviated",
                        "NovemberAbbreviated",
                        "DecemberAbbreviated"];
var dayNameByIndex = ["Sunday",
                      "Monday",
                      "Tuesday",
                      "Wednesday",
                      "Thursday",
                      "Friday",
                      "Saturday"];