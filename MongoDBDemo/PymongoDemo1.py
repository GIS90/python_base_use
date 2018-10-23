# coding:utf-8


import pymongo

connMongo = pymongo.MongoClient(host='127.0.0.1', port=27017, connect=True)

print connMongo

db = connMongo.test
collection = db.test

print db
print collection
