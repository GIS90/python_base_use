# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
mongodb 数据库缓存
------------------------------------------------
"""
import zlib
from datetime import datetime, timedelta

from bson.binary import Binary
from pymongo import MongoClient

try:
    import cPickle as pickle
except ImportError:
    import pickle

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/12"


class MongoCace(object):
    """
    mongo database cache
    """

    def __init__(self, client=None, expire_day=30):
        """
        MongoCache class initation
        :param client: mongo database client
        :param expire_day: data store time
        :return: None
        """
        assert isinstance(expire_day, int)

        self.client = MongoClient('127.0.0.1', 27017) if client is None else client
        self.expire_time = timedelta(days=30)
        self.db = self.client.spider_cache
        self.db.webhtml.create_index('timestamp', expireAfterSeconds=expire_day.total_seconds())

    def __getitem__(self, url):
        """
        get url result
        :param url: html url
        :return: html result
        """
        record = self.db.webhtml.find_one({'_id': url})
        if record:
            result = zlib.decompress(record['result'])
            return pickle.loads(result)
        else:
            raise KeyError('%s is not exist' % url)

    def __setitem__(self, url, result):
        """
        set url result
        :param url: html url
        :param result: html result
        :return: None
        """
        record = {'result': Binary(zlib.compress(pickle.dumps(result))), 'timestamp': datetime.utcnow()}
        self.db.webpage.update({'_id': url}, {'$set': record}, upsert=True)

    def __contains__(self, item):
        try:
            self[url]
        except KeyError:
            return False
        else:
            return True

    def clear(self):
        """
        clear mongodb data
        :return:
        """
        self.db.webhtml.drop()
