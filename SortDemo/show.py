# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import numpy as np
import matplotlib.pyplot as plt

from core.dbhandler import *


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/2"


x = [i for i in range(10)]
print x
y1 = np.sin(x)
y2 = np.sin(3 * x)

host = "localhost"
port = 3306
user = "root"
password = "123456"
database = "test"
dbhandle = DBHandler(host=host,
                     port=port,
                     user=user,
                     password=password,
                     database=database)
dbhandle.open()
charu = []
guibing = []
maopao = []
xier = []
xuanze = []
sql = 'select charu_time from sortcord'
charu_rlts = dbhandle.query(sql, 2)
for rlt in charu_rlts:
    charu.append(rlt[0])
sql = 'select guibing_time from sortcord'
guibing_rlts = dbhandle.query(sql, 2)
for rlt in guibing_rlts:
    guibing.append(rlt[0])
sql = 'select maopao_time from sortcord'
maopao_rlts = dbhandle.query(sql, 2)
for rlt in maopao_rlts:
    maopao.append(rlt[0])
sql = 'select xier_time from sortcord'
xier_rlts = dbhandle.query(sql, 2)
for rlt in xier_rlts:
    xier.append(rlt[0])
sql = 'select xuanze_time from sortcord'
xuanze_rlts = dbhandle.query(sql, 2)
for rlt in xuanze_rlts:
    xuanze.append(rlt[0])


print len(x)
print len(charu)
print len(xuanze)


fig, ax = plt.subplots()
ax.fill(x, charu, 'b', x, xuanze, 'r', alpha=0.3)
plt.show()





