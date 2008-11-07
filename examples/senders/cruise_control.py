#!/usr/bin/env python
import eventter
import sys

status = sys.argv[1]
message = sys.argv[2]

title = 'Cruise Control Build %s' % status
eventter.send(title=title, message=message)
