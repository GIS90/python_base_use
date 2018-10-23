# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
识别网站所用技术,主要用到了builtwith
------------------------------------------------
"""
import builtwith


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/5"

url = 'http://example.webscraping.com'
rlt = builtwith.parse(url)
print type(rlt)
for k, v in rlt.items():
    print '%s: %s' % (k, v)





