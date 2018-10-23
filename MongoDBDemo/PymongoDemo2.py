# coding:utf-8

import pymongo
import datetime
import codecs
import os

print 'Python Operate MongoDB .........'
# 创建一个文本存储获取的信息
filePath = r'E:\region'
fileName = 'mongoTest.txt'
f = os.path.join(filePath, fileName)
if os.path.exists(f):
    os.unlink(f)
f_w = codecs.open(filename=f, mode='w', encoding='utf-8')

dt = datetime.datetime.now()
formatterTime = '%Y-%m-%d-%H-%M-%S%p'
now = dt.strftime(formatterTime)
timeInfo = 'Start Time Is : %s .' % now
f_w.write(timeInfo)
f_w.write('\r\n')
print timeInfo

# 获取数据库的连接对象
connObj = pymongo.MongoClient('localhost', 27017)
# 获取所有数据库名称
dbs = connObj.database_names()
dbsNew = ' '.join(dbs)
db = connObj.gps
dbsInfo = 'Current DataBase List : %s' % dbsNew
print dbsInfo.decode('utf-8')
f_w.write(' '.join(dbs))
# 获取当前数据库的集合cols
cols = db.collection_names()
print 'Current Collections List : %s' % cols
col = db.metaGPS
results = col.find()

for rs in results:
    print rs
