# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 支持代理
------------------------------------------------
"""
import urllib2
import urlparse


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/5"


def download(url, user_agent='wswp', proxy=None, num_retries=3):
    assert isinstance(url, basestring)
    assert isinstance(user_agent, basestring)
    assert isinstance(proxy, basestring)
    assert isinstance(num_retries, int)

    print 'download url: %s' % url
    headers = {'User-agent': user_agent}
    request = urllib2.Request(url=url, headers=headers)

    opener = urllib2.build_opener()
    html = None
    if proxy:
        proxy_params = {urlparse.urlparse(url).scheme: proxy}
        opener.add_handler(urllib2.ProxyHandler(proxy_params))
    try:
        html = opener.open(request).read()
    except urllib2.URLError as e:
        print 'download error: %s' % e.reason
        html = None
        if hasattr(e, 'code') and 500 <= e.code <= 600:
            html = download(url, user_agent, proxy, num_retries - 1)
    else:
        return html






