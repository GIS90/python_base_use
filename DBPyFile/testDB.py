#coding:utf-8


#from Core.DBHandler import *
import cx_Oracle

import sqlite3

dbpath=r'D:\Py_File\test.db'

conn=sqlite3.connect(dbpath)
cursor=conn.cursor()
cursor.execute("select * from test")
for i in cursor.fetchall():
    print i