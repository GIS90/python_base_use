# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/21"

import MySQLdb
from DBUtils.PooledDB import PooledDB

pool = PooledDB(MySQLdb, 5, host='127.0.0.1', user='root', passwd='123456', db='ty', port=3306)  # 5为连接池里的最少连接数

conn = pool.connection()  # 以后每次需要数据库连接就是用connection（）函数获取连接就好了
cur = conn.cursor()
SQL = "select * from dir"
r = cur.execute(SQL)
r = cur.fetchall()
print r
cur.close()
conn.close()
