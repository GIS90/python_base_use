# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import redis

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/21"


pool = redis.ConnectionPool(host='127.0.0.1', port=6379, db=0)
r = redis.StrictRedis(connection_pool=pool)

# set方法
# print r.set('foo', 'bar')
# print r.setnx('foo1', 'bar')
# print r.mset({'k1': 'v1', 'k2': 'v2'})

# get方法
# print r.getset('foo', '00b')
# r.set('foo', 'asdfghjkl')
# print r.getrange('foo', 2, 5)
#
# r.set('k1', '123')
# for i in '123':
#     print i, ord(i), bin(ord(i))
#
# r.setbit('k1', 2, 0)
# print r.get('k1')
# print r.getbit('k1', 2)
r.set('foo', 'bar')
r.append('foo', '_bar')
print r.get('foo')
print r.getset('foo', 'bar_bar_bar')
print r.get('foo')
print r.strlen('foo')

