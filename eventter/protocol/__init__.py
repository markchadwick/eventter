import simplejson

class Protocol(object):
    def send(self, title, message):
        abstract

    def _title_and_message_to_packet(self, title, message):
        return simplejson.dumps({'title': title, 'message': message})

    def _packet_to_title_and_message(self, packet):
        msg = simplejson.loads(packet)
        title = None
        message = None
        
        if 'title' in msg:
            title = msg['title']
        if 'message' in msg:
            message = msg['message']
    
        return title, message

def default_protocol():
    from eventter.protocol.udp import UDPProtocol
    return UDPProtocol