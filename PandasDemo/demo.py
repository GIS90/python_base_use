# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: demo.py
@time: 2016/8/12 19:40
@describe: 
@remark: 
------------------------------------------------
"""

import pandas


df = pandas.read_csv("test.csv")

print df.head()
print df.tail()

print df.columns
print df.index

print df.T

