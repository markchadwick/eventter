#!/usr/bin/env python

"""
eventter receiver that posts received messages to an IRC channel.
Requires the Python IRC library (easy_install python-irclib)
"""

import eventter
import irclib
import sys

class IRCRelayReceiver(irclib.SimpleIRCClient):
    """
    Receive eventter messages and propagate them via IRC.
    """
    def __init__(self, irc_server, nickname, channel):
        irclib.SimpleIRCClient.__init__(self)
        self.server = irc_server
        self.nickname = nickname
        self.channel = channel
        self.connected = False

        try:
            self.connect(self.server, 6667, self.nickname)
        except irclib.ServerConnectionError:
            print >> sys.stderr, 'Cannot connect to IRC server "%s"' %\
                  irc_server
            raise x

        self.start()

    def on_welcome(self, connection, event):
        if irclib.is_channel(self.channel):
            connection.join(self.channel)
        else:
            print >> sys.stderr, '"%s" is not a valid IRC channel' %\
                  self.channel
            sys.exit(1)

    def on_join(self, connection, event):
        self.connected = True
        eventter.on_message(self.on_eventter_message)

    def on_disconnect(self, connection, event):
        sys.exit(0)

    def on_eventter_message(self, title, message):
        # Remove embedded newlines.
        message = ' '.join([line.strip() for line in message.split('\n')])
        self.connection.privmsg(self.channel, title + ": " + message)
        
if __name__ == '__main__':
    IRCRelayReceiver(irc_server=sys.argv[1],
                     nickname=sys.argv[2],
                     channel=sys.argv[3])

