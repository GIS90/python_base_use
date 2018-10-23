# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
set集合
------------------------------------------------
"""
import redis


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/21"


pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)


r.sadd('set_name', 'set')
r.sadd('set_name', 'aa', 'bb', 'cc')

print r.smembers('set_name')
print r.scard('set_name')

r.sadd('set_name3', 'aa', 'bb')
r.sadd('set_name1', 'aa', 'bbb')
r.sadd('set_name2', 'aa', 'bbv')
print r.sdiff('set_name3', 'set_name1')


