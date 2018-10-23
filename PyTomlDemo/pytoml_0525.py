# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/5/25'
"""

import pytoml


tf = file('config1.toml')

tfc = pytoml.load(tf)

print len(tfc)
print tfc.keys()
for k, v in tfc.items():
    print str(k) + '-------' + str(v)
print tfc['owner']['name']
