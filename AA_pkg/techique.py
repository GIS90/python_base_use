# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: techique.py
@time: 2016/8/11 9:39
------------------------------------------------
"""

from __future__ import division

if __name__ == '__main__':
    print 1 / 2

iterable = [1, 2, 3, 5]
for i, item in enumerate(iterable):
    print i, item

from pprint import pprint

my_dict = {i: i * i for i in xrange(100)}
pprint(my_dict)

import sys
import inspect
print inspect.stack()
print sys.argv
print sys.path
print sys.version
print sys.version_info
import os

print os.path.split(os.path.realpath(__file__))[0]
print os.path.abspath(os.path.split(os.path.realpath(__file__))[0])

print sys.platform
print os.name
import json




s = {u'data': {u'userId': u'mingliang.gao', u'userInfo': {u'dept': [u'\u5e73\u53f0\u4e8b\u4e1a\u90e8', u'\u6280\u672f\u4fdd\u969c\u4e2d\u5fc3', u'Isdev', u'\u5185\u7f51\u529e\u516c\u7cfb\u7edf', u''], u'manager': u'\u53f2\u9756\u7476', u'ad_cn': u'\u9ad8\u660e\u4eae', u'name': u'\u9ad8\u660e\u4eae', u'company': u'qunar'}}, u'userId': u'mingliang.gao', u'ret': True}

for k, v in s.get('data').get('userInfo').iteritems():
    print k, v





