#!/usr/bin/env python

"""
eventter receiver that posts received messages to standard output. More of
an exercise in writing the simplest possible receiver than anything else.
"""

import eventter

class TextReceiver(object):
    """
    Receive eventter messages and write them to stdout.
    """
    def __init__(self):
        eventter.on_message(self.on_message)

    def on_message(self, title, message):
        sep = '*' * len(title)
        print '%s\n%s\n%s\n\n%s' % (sep, title, sep, message)

        
if __name__ == '__main__':
    TextReceiver()

