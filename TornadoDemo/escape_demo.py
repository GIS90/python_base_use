# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2016/11/28"

if __name__ == '__main__':
    pass

import cgi

s1 = "Hello <strong>world</strong>"
s2 = cgi.escape(s1)

print s2
