# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: demo_1.py
@time: 2016/8/31 9:47
@describe: 
@remark: 
------------------------------------------------
"""

import pandas as pd
import numpy as np


# s = pd.Series([1, 2, 3, 4, 5, 6, 7])
# print s
# dates = pd.date_range('20160101', periods=10)
# for i in dates:
#     print i
#
#
# df = pd.DataFrame(np.random.randn(10, 4), index=dates, columns=list("ABCD"))
# print df


reader = pd.read_csv('test.csv', iterator=True)
try:
    df = reader.get_chunk(100000000)
except StopIteration:
    print "Iteration is stopped."

print df.head(3)
print df.tail(3)
print df.describe
