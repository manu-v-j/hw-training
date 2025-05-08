(function() {
	var _hasDeleteListenersOnUnloadEvent = false;
	var _listeners = {};
	var _counter = 0;

	function _Listener(source, event, handler) {
		if (source == null)
			reliance.throwError('[reliance.event] Source not found for ' + event + ' event.')

		this.source = source;
		this.event = event;
		this.handler = handler;

		_listeners[_counter] = this;
		_counter++;
	}

	function addListener(source, event, handler) {
		event = event.toLowerCase();
		var listener = new _Listener(source, event, handler);

		// Register an unload event hanlder to clear all the events.
		if (!_hasDeleteListenersOnUnloadEvent) {
			if (window.addEventListener) {
				window.addEventListener('unload', _deleteAllListeners, false);
			} else {
				window.attachEvent('onunload', _deleteAllListeners);
			}
			_hasDeleteListenersOnUnloadEvent = true;
		}

		return listener;
	}

	function addDomListener(source, event, handler) {
		event = event == 'unload' ? 'xunload' : event;
		try {
			var listener = addListener(source, event, handler);

			if (event != 'xunload') {
				if (window.addEventListener) {
					source.addEventListener(event, handler, false);
				} else {
					handler = callback(source, handler);
					source.attachEvent('on' + event, handler);
				}
			}

			return listener;
		} catch (ex) {
			reliance.throwError('[reliance.event.addDomListener] ' + ex);
		}
	}

	function bind(source, event, object, handler) {
		var args = _getArguments(arguments, 4);
		if (args.length > 0) {
			handler = callbackArgs.apply(null, [object, handler].concat(args));
		} else {
			handler = callback(object, handler);
		}
		return addListener(source, event, handler);
	}

	function bindDom(source, event, object, handler) {
		var args = _getArguments(arguments, 4);
		if (args.length > 0) {
			handler = callbackArgs.apply(null, [object, handler].concat(args));
		} else {
			handler = callback(object, handler);
		}
		return addDomListener(source, event, handler);
	}

	function removeListener(listener) {
		for (var l in _listeners)
			if (_listeners[l] == listener) {
				delete _listeners[l]
				break;
			}

		try {
			if (window.removeEventListener) {
				if (listener && listener.source.removeEventListener)
					listener.source.removeEventListener(listener.event, listener.handler, false);
			} else {
				if (listener && listener.source.detachEvent)
					listener.source.detachEvent('on' + listener.event, listener.handler);
			}
		} catch (ex) { }
	}

	function clearListeners(source, event) {
		for (var l in _listeners)
			if ((_listeners[l].source == source && _listeners[l].event == event.toLowerCase()) || (source == window && event == 'unload' && _listeners[l].event == 'xunload'))
				removeListener(_listeners[l]);
	}

	function clearInstanceListeners(source) {
		for (var l in _listeners)
			if (_listeners[l].source == source)
				removeListener(_listeners[l]);
	}

	function trigger(source, event) {
		var args = _getArguments(arguments, 2);
		for (var l in _listeners)
			if (_listeners[l].source == source && _listeners[l].event == event.toLowerCase()) {
				_listeners[l].handler.apply(source, args);
			}
	}

	function callback(object, handler) {
		return function() { return handler.apply(object, _getArguments(arguments, 0)); }
	}

	function callbackArgs(object, handler) {
		var args = _getArguments(arguments, 2);
		return function() { var argIndex; try { argIndex = arguments[0] instanceof Event ? 1 : 0 } catch (e) { argIndex = 0 } return handler.apply(object, args.concat(_getArguments(arguments, argIndex))); }
	}

	function _deleteAllListeners() {
		for (var l in _listeners)
			if (_listeners[l].event == 'xunload')
				_listeners[l].handler.apply();

		for (var l in _listeners)
			removeListener(_listeners[l]);

		if (window.removeEventListener) {
			window.removeEventListener('unload', _deleteAllListeners, false);
		} else {
			window.detachEvent('onunload', _deleteAllListeners);
		}
	}

	function _getArguments(argArray, startIndex) {
		var args = [];
		for (var i = startIndex; i < argArray.length; i++)
			args.push(argArray[i]);
		return args;
	}

	var _symbols = [
		['addListener', addListener],
		['addDomListener', addDomListener],
		['bind', bind],
		['bindDom', bindDom],
		['removeListener', removeListener],
		['clearListeners', clearListeners],
		['clearInstanceListeners', clearInstanceListeners],
		['trigger', trigger],
		['callback', callback],
		['callbackArgs', callbackArgs]
	];
	window.reliance_exportSymbols('reliance.event', _symbols);
})();