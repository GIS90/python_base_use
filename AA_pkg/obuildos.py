# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""


import os



print os.error

print 'system: ', os.name
print 'env: ', os.environ

print os.getcwd()

print getattr(os, 'ctermid', 'xxxx')

print hasattr(os, 'fork')
print os.umask(1)
print os.getpid()



