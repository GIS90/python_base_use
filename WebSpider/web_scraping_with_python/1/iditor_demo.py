# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
ID遍历爬虫
------------------------------------------------
"""
from scrapy import download
import itertools


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/5"


num_errors = 0
max_errors = 5

for page in itertools.count(1):
    url = 'http://example.webscraping.com/view/-%d' % page
    html = download(url)
    print url
    if html is None:
        num_errors += 1
        if num_errors == max_errors:
            break
    else:
        num_errors = 0






