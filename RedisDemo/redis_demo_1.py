# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
redis 的操作集合
------------------------------------------------
"""
import redis

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/21"

pool = redis.ConnectionPool(host='192.168.2.181', port=7002, db=0)
r = redis.Redis(connection_pool=pool)

print r
print r.get('name')



