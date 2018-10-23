# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
redis 的list的存储

------------------------------------------------
"""
import redis

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/21"

pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

r.lpush('ln', 2, 3, 4, 5, 65, 2)
print r.rpush('ln', 1)
print r.lpushx('ln', 22)
print r.llen('ln')
r.linsert('ln', 'BEFORE', 3, 123)
r.lset('ln', 0, 'test')
print r.lpop('ln')
print r.lindex('ln', 4)



