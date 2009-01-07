#!/usr/bin/env python

"""
eventter receiver that posts received messages via the Windows Snarl service.
Snarl is an open source Growl-like tool for Windows. See
http://www.fullphat.net/index.php

You'll need Alexander Lash's snarl.py, from
http://alexander.lash.googlepages.com/snarl.py

Lash's snarl.py, in turn, requires pywin32. See
http://sourceforge.net/projects/pywin32/
"""

import eventter
import snarl

class SnarlReceiver(object):
    """
    Receive eventter messages and propagate them via Growl.
    """
    def __init__(self):
        eventter.on_message(self.on_message)

    def on_message(self, title, message):
        message = ' '.join([line.strip() for line in message.split('\n')])
        snarl.snShowMessage(title, message, timeout=3)
        
if __name__ == '__main__':
    SnarlReceiver()

