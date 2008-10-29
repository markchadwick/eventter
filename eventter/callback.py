from threading import Thread

class Callback(Thread):
    def __init__(self, protocol, callback):
        Thread.__init__(self)
        
        self.protocol = protocol
        self.callback = callback
    
    def run(self):
        self.protocol.on_message(self.callback)
        
    def stop(self):
        self.protocol.kill()