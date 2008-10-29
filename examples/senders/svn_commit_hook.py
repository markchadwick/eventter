#!/usr/bin/env python
import eventter
import sys
import os

SVNLOOK='/usr/bin/svnlook'

class SVNNotification(object):
    """
    Roughly ported from::
    http://hipstersinc.com/blog/2007/2/28/growl_subversion_postcommit_notification/
    """
    def __init__(self, path, revision, opts={}):
        self.path = path
        self.revision = revision
        self.svn_look = SVNLOOK

        self._author = self.lookup('author')
        self._log    = self.lookup('log')
        self._date   = self.lookup('date')
        self._changed= self.lookup('changed')

    def send(self):
        title   = "%s committed revision %s" % (self._author, self.revision)
        eventter.send(title=title, message=self._log)

    def lookup(self, param):
        cmd = "%s %s %s -r %s" % (
            self.svn_look,
            param,
            self.path,
            self.revision
        )
        
        lines = []
        for line in os.popen(cmd):
            lines.append(line.strip())
            
        return '\n'.join(lines)

if __name__ == '__main__':
    args = sys.argv
    svn = SVNNotification(args[1], args[2])
    svn.send()