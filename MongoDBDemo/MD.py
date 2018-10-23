# -*- coding: utf-8 -*-
"""
__author__ = 'localhost'
__time__ = '2016/7/25'
"""

import pymongo


mgConn = pymongo.MongoClient(host='127.0.0.1', port=27017)
mgDB = mgConn.sde
mgCol = mgDB.path


print mgConn.database_names()
print mgDB.collection_names()
print mgCol.find()
