//reliance.load('platform');
(function() {
	var _userAgent = navigator.userAgent.toLowerCase();
	var _scrollbarWidth;

	function isIE() { return _userAgent.indexOf('msie') != -1 }
	function isSafari() { return _userAgent.indexOf('safari') != -1 }
	function isChrome() { return _userAgent.indexOf('chrome') != -1 }
	function isFirefox() { return _userAgent.indexOf('firefox') != -1 }
	function isWebKit() { return _userAgent.indexOf('webkit') != -1 }
	function isMobile() { return _userAgent.indexOf('mobile') != -1 }
	function supportsNativePng() {
		if (!isIE()) return true;
		var regex = new RegExp('msie ([0-9]{1,}[\.0-9]{0,})');
		if (regex.exec(_userAgent) != null)
			return parseFloat(RegExp.$1) > 6;
	}
	function inputWidthCorrection() {
		if (isIE()) return 6;
		if (isFirefox() || isChrome()) return 4;
		if (isSafari()) return 7;
		return 0;
	}
	function scrollbarWidthCorrection() { 
		if (!_scrollbarWidth) { 
			var doc = document;
			var body = doc.body;
			var div = doc.createElement('div'); 
			div.appendChild(doc.createTextNode(',')); 
			var container = div.cloneNode(false); 
			container.style.cssText = 'width:100px;overflow:scroll;position:absolute;left:-100px'; 
			container.appendChild(div); 
			body.appendChild(container); 
			_scrollbarWidth = container.offsetWidth - container.clientWidth; 
			body.removeChild(container);
		} 
		return _scrollbarWidth;
	}	

	var _symbols = [
		['isIE', isIE],
		['isSafari', isSafari],
		['isChrome', isChrome],
		['isFirefox', isFirefox],
		['isWebKit', isWebKit],
		['isMobile', isMobile],
		['supportsNativePng', supportsNativePng],
		['inputWidthCorrection', inputWidthCorrection],
		['scrollbarWidthCorrection', scrollbarWidthCorrection]
	];
	window.reliance_exportSymbols('reliance.browser', _symbols);
})();