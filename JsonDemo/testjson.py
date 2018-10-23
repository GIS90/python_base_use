# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/7/12'
"""


import json


f = file("busline.js")
s = json.load(f)
print s
f.close