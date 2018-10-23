# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
增加文件缓存功能
------------------------------------------------
"""
import os
import sys
import re
import urlparse
import shutil
import zlib
from datetime import datetime
from datetime import timedelta
try:
    import cPickle as pickle
except ImportError:
    import pickle
from link_crawler import link_crawler


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/12"


class DiskCache(object):
    """
    data store disk cache
    """
    def __init__(self, cache_dir, expire_time=30, compress=True):
        """
        DiskCache class initation
        set cache_dir, expire_time, compress
        :param cache_dir: url cache dir
        :param expire_time: url data store expire time, unit is day
        :param compress: url data is or not compress
        :return: None
        """
        assert isinstance(cache_dir, basestring)
        assert isinstance(expire_time, int)
        assert isinstance(compress, bool)

        self.cache_dir = cache_dir
        self.expire = timedelta(days=expire_time)
        self.compress = compress


    def __getitem__(self, url):
        assert isinstance(url, basestring)

        def has_expire(timestamp):
            return datetime.now() > timestamp + self.expire

        path = self.url_to_path(url)
        if os.path.exists(path):
            with open(path, 'rb') as f:
                data = f.read()
                if self.compress:
                    data = zlib.decompress(data)
                result, timestamp = pickle.loads(data)
                if has_expire(timestamp):
                    raise KeyError('%s is expire' % url)
                return result
        else:
            raise KeyError('%s is not exist' % url)

    def __setitem__(self, url, result):
        assert isinstance(url, basestring)

        path = self.url_to_path(url)
        folder = os.path.dirname(path)
        if not os.path.exists(folder):
            os.makedirs(folder)

        data = pickle.dumps((result, datetime.utcnow()))
        if self.compress:
            data = zlib.compress(data)
        with open(path, 'wb') as f:
            f.write(data)

    def __delitem__(self, url):
        assert isinstance(url, basestring)

        path = self.url_to_path(url)
        try:
            os.remove(path)
            os.removedirs(os.path.dirname(path))
        except OSError:
            pass

    def url_to_path(self, url):
        """
        url tranfer to path of disk cache
        :param url:
        :return: path
        """
        assert isinstance(url, basestring)

        components = urlparse.urlsplit(url)
        path = components.path
        if not path:
            path = '/index.html'
        elif path.endswith('/'):
            path += 'index.html'

        filename = components.netloc + path + components.query
        pattern = '[^/0-9a-zA-Z\-.,;_]'
        filename = re.sub(pattern, '_', filename)
        filename = '/'.join(segment[:255] for segment in filename.split('/'))

        return os.path.join(self.cache_dir, filename)

    def clear(self):
        """
        clear disk cache
        :return:
        """
        if os.path.exists(self.cache_dir):
            shutil.rmtree(self.cache_dir)


if __name__ == '__main__':
    link_crawler('http://example.webscraping.com/', '/(index|view)', cache=DiskCache(cache_dir='cache', compress=False))

