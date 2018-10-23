# -*- coding: utf-8 -*-



import sys, os
print "script: sys.argv[0] is", repr(sys.argv[0])
print "script: __file__ is", repr(__file__)
print __file__
print "script: cwd is", repr(os.getcwd())

print '-----------------------------------------'
print os.path.dirname(os.path.abspath(os.getcwd()))
print os.path.dirname(os.getcwd())
print os.path.pardir
print os.path.join(os.path.dirname("__file__"),os.path.pardir)
print os.path.abspath(os.path.join(os.path.dirname("__file__"),os.path.pardir))