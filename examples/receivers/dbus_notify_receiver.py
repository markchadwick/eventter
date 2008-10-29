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