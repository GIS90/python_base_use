# -*- coding: utf-8 -*-

import pymongo
import datetime

mgClient = pymongo.MongoClient(host='localhost', port=27017)
mg_db = mgClient.sde
mg_col = mg_db.project
post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()
        }
mg_col.insert(post)
print 'success'
for i in mg_col.find():
    print i
