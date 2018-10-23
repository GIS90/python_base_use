# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
如果抓取网站的速度过快，就会面试呗封禁或者是造成
服务器过载的风险。为了降低这些风险，我们在2次直接
的添加延时，从而对爬虫限速。
------------------------------------------------
"""
import urlparse
import urllib2
import time
import datetime


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/5"


class Throttle(object):

    def __init__(self, delay):
        assert isinstance(delay, int)

        self.delay = delay
        self.domains = {}

    def wait(self, url):
        assert isinstance(url, basestring)

        domain = urlparse.urlparse(url).netloc
        lastime_accessed = self.domains.get(domain)

        if self.delay > 0 and lastime_accessed is not None:
            now = datetime.datetime.now()
            sleep_time = self.delay - (now - lastime_accessed).seconds
            if sleep_time > 0:
                time.sleep(sleep_time)
        self.domains[domain] = datetime.datetime.now()




