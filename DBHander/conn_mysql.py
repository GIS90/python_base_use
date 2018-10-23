# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: conn_mysql.py
@time: 2016/8/29 19:21
@describe: 
@remark: 
------------------------------------------------
"""
import MySQLdb

# 建立和数据库系统的连接
conn = MySQLdb.connect(host='127.0.0.1', user='root', passwd='123456', db="test", charset="utf8")

# 获取操作游标
cursor = conn.cursor()
# 执行SQL,创建一个数据库.
cursor.execute("""select * from allnetname""")


results = cursor.fetchall()
print results
if not results:
    print "None"
else:
    print 1
# for r in results:
#     print r
    # for i in r:
    #     print i


#
# sql = 'drop table if exists busline_copy '
# n = cursor.execute(sql)
# print n
# conn.close()
