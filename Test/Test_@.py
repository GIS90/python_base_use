# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/9'
"""

myDict = {i: i * i for i in xrange(10)}
myDictdata = (
    "this is a string", [1, 2, 3, 4], ("more tuples",
    1.0, 2.3, 4.5), "this is yet another string"
    )

import pprint
print myDictdata
pprint.pprint(myDictdata)
