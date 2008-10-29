from eventter.protocol import Protocol

import socket
import traceback

HOST = ''
PORT = 51552
DST  = '255.255.255.255'

class UDPProtocol(Protocol):
    def send(self, title, message):
        message = self._title_and_message_to_packet(title, message)

        self._alive = True
        self._setup_sending_socket()
        self.sock.sendto(message, (DST, PORT))
        self._teardown_sending_socket()
        
    def on_message(self, callback):
        self.csock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.csock.bind(("0.0.0.0", PORT))
        
        while True:
            msg, addr = self.csock.recvfrom(PORT)
            title, message = self._packet_to_title_and_message(msg)
            callback(title=title, message=message)

    def kill(self):
        self._alive = False

    def _setup_sending_socket(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

    def _teardown_sending_socket(self):
        try:
            self.sock.shutdown(1)
        except socket.error:
            pass
            