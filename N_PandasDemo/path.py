# -*- coding: utf-8 -*-

import os
import sys

print '__file__ = ' + __file__
print 'os.path.abspath = ' + os.path.abspath(__file__)
print 'os.path.realpath = ' + os.path.realpath(__file__)
print 'os.getcmd = ' + os.getcwd()
print 'sys.path = %s' % sys.path[0]
print 'sys.argv = %s' % sys.argv[0]
print 'os.path.basename = %s' % os.path.basename(__file__)
print 'os.path.dirname = %s' % os.path.dirname(__file__)
print 'os.stat = %s' % os.stat(__file__)
print 'os.path.getsize = %s' % os.path.getsize(__file__)
