# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
web网络爬虫开始
------------------------------------------------
"""
import urllib2

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/5"

NUM_RETRIES = 3


def download(url, user_agent='', num=NUM_RETRIES):
    assert isinstance(url, basestring)

    print 'download url: %s' % url

    headers = {'User_agent': user_agent}
    request = urllib2.Request(url=url, headers=headers)
    try:
        response = urllib2.urlopen(request)
        html = response.read()
    except urllib2.URLError as e:
        print 'download error: %s' % e.reason
        if num > 0:
            # 如果下载错误代码是500-600，进行重新下载
            if hasattr(e, 'code') and 500 <= e.code <= 600:
                return download(url, user_agent, num - 1)


url = 'http://example.webscraping.com/'
user_agent = 'wswp'
print download(url, user_agent, NUM_RETRIES)
