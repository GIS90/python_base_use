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

r.hset('dic_name', 'a1', 'a1')
r.hset('dic_name', 'a2', 'a2')
r.hset('dic_name', 'a3', 'a3')
r.hset('dic_name', 'a4', 'a4')
print r.hget('dic_name', 'a1')
print r.hgetall('dic_name')

b = {'b1': "b1", 'b2': "b2"}
r.hmset('dic_name', b)
print r.hgetall('dic_name')

print r.hlen('dic_name')
print r.hkeys('dic_name')
print r.hvals('dic_name')

print r.hexists('dic_name', 'a1')
print r.hexists('dic_name', 'ab')
print r.hdel('dic_name', 'a2')
print r.hdel('dic_name', 'a2')

print r.hscan('dic_name')


