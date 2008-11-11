#!/usr/bin/env python

"""
eventter receiver that posts received messages via the Mac OS X Growl daemon.
Requires the Growl distribution (http://growl.info) and the Python bindings
from the Growl Developer SDK (http://growl.info/documentation/developer/).
"""

import eventter
import Growl

class GrowlReceiver(object):
    """
    Receive eventter messages and propagate them via Growl.
    """
    def __init__(self):
        
        self.growl = Growl.GrowlNotifier(
            applicationName='eventter',
            notifications=[Growl.GROWL_NOTIFICATION]
        )
        self.growl.register()
        eventter.on_message(self.on_message)

    def on_message(self, title, message):
        # Remove embedded newlines; let the Growl notifier do the wrapping.
        # Note: Empty lines (i.e., paragraphs) are preserved.
        message = ' '.join(['\n\n' if len(line) == 0 else line.strip()
                                   for line in message.split('\n')])
        self.growl.notify(Growl.GROWL_NOTIFICATION, title, message)

        
if __name__ == '__main__':
    GrowlReceiver()

