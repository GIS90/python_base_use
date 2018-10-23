# -*- coding: utf-8 -*-

import redis

rpool = redis.ConnectionPool(host='127.0.0.1 ', port=6379)
r = redis.Redis(connection_pool=rpool)
try:

    key = r.randomkey()
    print r.get(key)

except:
    print 'error'
