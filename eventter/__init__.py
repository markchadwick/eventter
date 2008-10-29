from eventter.protocol import default_protocol
from eventter.callback import Callback

CALLBACKS = {}

def send(title, message, protocol=None):
    if protocol is None:
        protocol = default_protocol()()
        
    protocol.send(title=title, message=message)

def on_message(callback, protocol=None):
    if protocol is None:
        protocol = default_protocol()()
        
    callback_thread = Callback(protocol, callback)
    callback_thread.start()
    
    CALLBACKS[callback] = callback_thread
    
def remove_callback(callback):
    if callback in CALLBACKS:
        CALLBACKS[callback].stop()
        del CALLBACKS[callback]