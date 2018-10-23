# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
具有缓存功能的下载类
下载类

------------------------------------------------
"""
import random
import socket
import time
import urllib2
import urlparse
from datetime import datetime

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/10"

DEAULT_USER_AGENT = 'wswp'
DEAULT_DEALY = 5
DEAULT_NUM_RETRIES = 3
DEAULT_TIMEOUT = 60


class Throttle(object):
    """
    use to download delay time
    """
    def __init__(self, delay):
        """
        set url download delay time in order to
        avoid download limit
        :param delay: delay time
        :return: None
        """
        assert isinstance(delay, int)

        self.delay = delay
        self.domains = {}

    def wait(self, url):
        """
        execute delay time if accessed else None
        :param url: accessed url
        :return: None
        """
        assert isinstance(url, basestring)

        try:
            domain = urlparse.urlparse(url).netloc
            last_time_accessed = self.domains.get(domain)
            if self.delay > 0 and last_time_accessed is not None:
                sleep_time = self.delay - (datetime.now() - last_time_accessed).seconds
                time.sleep(sleep_time) if sleep_time > 0 else None
        except Exception as e:
            print 'throttle wait error: %s' % e.message
        else:
            self.domains[domain] = datetime.now()


class Downloader(object):
    """
    downloader class
    """
    def __init__(self, delay=DEAULT_DEALY, user_agent=DEAULT_USER_AGENT, proxies=None, num_retries=DEAULT_NUM_RETRIES,
                 timeout=DEAULT_TIMEOUT, opener=None, cache=None):
        assert isinstance(delay, int)
        assert isinstance(user_agent, basestring)
        assert isinstance(num_retries, int)
        assert isinstance(timeout, int)

        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.opener = opener
        self.cache = cache
        socket.setdefaulttimeout(timeout)

    def __call__(self, url, *args, **kwargs):
        assert isinstance(url, basestring)

        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except Exception as e:
                pass
            else:
                if self.num_retries > 0 and 500 <= result['code'] <= 600:
                    result = None
        if result is None:
            self.throttle.wait(url)
            proxy = random.choice(self.proxies) if self.proxies else None
            header = {'User-agent': self.user_agent}
            result = self.download(url=url, header=header, proxy=proxy, num_retries=self.num_retries)
            if self.cache:
                self.cache[url] = result

        return result['html']

    def download(self, url, header=None, proxy=None, num_retries=3, data=None):
        """
        download url
        :param url: spider url
        :param header: spider url header
        :param proxy: spider url proxy
        :param num_retries: spider url retry download
        :param data: spider url query data
        :return: url read
        """
        assert isinstance(url, basestring)
        assert isinstance(num_retries, int)

        print 'download url: %s' % url
        request = urllib2.Request(url=url, headers=header or {}, data=data)
        opener = self.opener or urllib2.build_opener()
        if proxy:
            proxy_params = {urlparse.urlparse(url).scheme: proxy}
            opener.add_handler(urllib2.ProxyHandler(proxy_params))
        try:
            response = opener.open(request)
            html = response.read()
            code = response.code
        except Exception as e:
            print 'Downloader download error: %s' % e.message
            html = ''
            if hasattr(e, 'code'):
                code = e.code
                if num_retries > 0 and 500 <= code <= 600:
                    return self._get(url, header, proxy, num_retries - 1, data)
            else:
                code = None
        finally:
            result = {'html': html, 'code': code}
            return result

# url = 'http://example.webscraping.com'
# d = Downloader()
# print d.download(url)
