# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import time

import pandas as pd
import numpy as np

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/8"

flag = True
size = 100 * 100
chunks = []
data = r"E:\data\XY\trip_data.csv"

reader = pd.read_csv(data, iterator=True)
start = time.clock()

n = 0
while flag:
    try:
        chunk = reader.get_chunk(size)
        chunks.append(chunk)
        n += 1
        if n == 5: break
    except StopIteration:
        print "Iteration is stopped."

df = pd.concat(chunks, ignore_index=True)
print time.clock() - start
print df.dtypes
# print df.describe()
# print df.head(n=10)
