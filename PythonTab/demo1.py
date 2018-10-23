# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import mmap
import stat
import os
import time


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/13"

f = 'demo.bin'
# f = open('demo.bin', 'r+b')
# print f.fileno()
#
# m = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_WRITE)
# print m, type(m)

s = os.stat(f)

print s.st_size
print stat.S_ISREG(s.st_mode)
print time.localtime(s.st_atime)


from tempfile import TemporaryFile, NamedTemporaryFile

tf = TemporaryFile()
tf.write('abncd' * 1000)
print f





