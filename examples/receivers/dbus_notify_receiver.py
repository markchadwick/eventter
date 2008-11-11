#!/usr/bin/env python

import eventter
import dbus

class DbusReceiver(object):
    def __init__(self):
        self.bus = dbus.SessionBus()
        self.bus.get_object("org.freedesktop.DBus","/org/freedesktop/DBus")
        notifyService = self.bus.get_object(
                                'org.freedesktop.Notifications',
                                '/org/freedesktop/Notifications')
                                
        self.interface = dbus.Interface(
                                notifyService,
                                'org.freedesktop.Notifications')
                                
        eventter.on_message(self.on_message)

    def on_message(self, title, message):
        # Remove embedded newlines; let the Dbus notifier do the wrapping.
        # Note: Empty lines (i.e., paragraphs) are preserved.
        message = ' '.join(['\n\n' if len(line) == 0 else line.strip()
                                   for line in message.split('\n')])
        app = 'DbusGeneric'
        self.interface.Notify(
            app,
            0,
            '/usr/share/icons/gnome/scalable/categories/stock_internet.svg',
            title,
            message,
            [],
            {},
            -1)


        
if __name__ == '__main__':
    dbus = DbusReceiver()
