# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
webspider append function of file cache

use:
......
------------------------------------------------
"""
import inspect
import os
import re
import shutil
import sys
import urlparse
import zlib
from datetime import datetime, timedelta
from link_crawler import link_crawler
try:
    import cPickle as pickle
except ImportError:
    import pickle


def __get_curdir(self):
    """
    get current file dir
    :param self:
    :return: current folder
    """
    if getattr(sys, 'forzen', False):
        return os.path.dirname(os.path.abspath(__file__))
    else:
        curdir = os.path.dirname(inspect.getfile(inspect.currentframe()))
        return os.path.abspath(curdir)


class DiskCache(object):
    """
    data store disk cache
    """

    def __init__(self, cache_dir='cache', expire_day=30, compress=True):
        """
        DiskCache class initation
        set cache_dir, expire_time, compress
        :param cache_dir: url cache dir
        :param expire_time: url data store expire time, unit is day
        :param compress: url data is or not compress
        :return: None
        """
        assert isinstance(cache_dir, basestring)
        assert isinstance(expire_day, int)
        assert isinstance(compress, int)

        if not os.path.isdir(cache_dir):
            self.cache = os.path.abspath(os.path.join(__get_curdir() + cache_dir))
        else:
            self.cache = cache_dir
        self.expire_day = timedelta(days=expire_day)
        self.compress = compress

    def has_expire(self, timestamp):
        """
        calculate time delta
        :param timestamp:
        :return:
        """
        assert isinstance(timestamp, datetime)
        return datetime.now() > timestamp + self.expire_day

    def __getitem__(self, url):
        """
        get url cache
        :param url:
        :return: cache result
        """
        assert isinstance(url, basestring)

        path = self.url_to_path(url)
        if os.path.exists(path):
            with open(path, 'rb') as f:
                data = f.read()
                if self.compress:
                    data = zlib.decompress(data)
                result, timestamp = pickle.loads(data)
                if self.has_expire(timestamp):
                    raise KeyError('%s is expire' % url)
                return result
        else:
            raise KeyError('%s is not exist' % url)

    def __setitem__(self, url, result):
        """
        set url cache
        :param url:
        :param result:
        :return: None
        """
        assert isinstance(url, basestring)
        assert isinstance(result, dict)

        path = self.url_to_path(url)

        if not os.path.exists(path):
            os.makedirs(path)

        if result:
            data = pickle.dumps((result, datetime.now()))
            if self.compress:
                data = zlib.compress(data)
            with open(path, 'wb') as f:
                f.write(data)
        else:
            raise KeyError('%s is not result data' % url)

    def __delitem__(self, url):
        """
        del url
        :param key:
        :return:
        """
        path = self.url_to_path(url)
        try:
            os.remove(path)
            os.removedirs(path)
        except:
            raise KeyError('%s is not exist' % url)

    def url_to_path(self, url):
        """
        url tranfer to path of disk cache
        :param url:
        :return: path
        """
        assert isinstance(url, basestring)

        components = urlparse.urlparse(url)
        path = components.path
        if not path:
            path = '/index.html'
        elif path.endswith('/'):
            path += 'index.html'

        filename = components.netloc + path + components.query
        pattern = '[^/0-9a-zA-Z\-.,;_]'
        filename = re.sub(pattern, '_', filename)
        filename = '/'.join(segment[:255] for segment in filename.split('/'))

        return os.path.join(self.cache, filename)

    def clear(self):
        """
        clear disk cache
        :return:
        """
        if os.path.exists(self.cache):
            shutil.rmtree(self.cache)


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com/', '/(index|view)', cache=DiskCache(cache_dir='cache', compress=False))
