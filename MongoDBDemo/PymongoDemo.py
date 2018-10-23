# coding:utf-8


import pymongo

mgClient = pymongo.MongoClient(host='localhost', port=27017)
mg_mymongo = mgClient.mymongo
mymongo_col = mg_mymongo.col

print mgClient
print mg_mymongo
print mymongo_col
myDict = []
dict1 = {"name": "Lucy", "age": 20, "sex": "female", "job": "nurse"}
dict2 = {"name": "Lily", "age": 18, "sex": "female", "job": "nurse"}
dict3 = {"name": "Nihao", "age": 23, "sex": "female", "job": "nurse"}
myDict.append(dict1)
myDict.append(dict2)
myDict.append(dict3)
mymongo_col.insert_many(myDict)

print 'OK'
