# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/21'
"""

import pymssql

# server = "10.212.129.50\inst01"
# port = 1724
# user = "fcdsys"
# password = "#fcd-a504"
# dbs = 'Congest'

server = "localhost"
port = "1433"
user = "sa"
password = "123456"
dbs = 'qd_json'

conn = pymssql.connect(server, user, password)
print conn
sql = "select top 10 * from qd_json.dbo.cell"
cursor = conn.cursor()
cursor.execute(sql)
rlt = cursor.fetchall()
for i in rlt:
    print i

