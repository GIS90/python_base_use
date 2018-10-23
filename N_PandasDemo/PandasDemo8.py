# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import time
import pandas as pd

from pandas import Series
from pandas import DataFrame


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/14"


data = r'E:\data\XY\trips_period_worker.txt'
flag = True
size = 100 * 100
chunks = []

print 'start'
startime = time.clock()
reader = pd.read_table(data, header=0, iterator=True)
print type(reader)
#
# n = 1
# while flag:
#     try:
#         chunk = reader.get_chunk(size)
#         chunks.append(chunk)
#         if n == 5:
#             break
#         n += 1
#     except StopIteration:
#         flag = False
#         print 'Iterator is stop'
#
# df = pd.concat(chunks, ignore_index=True)
# endtime = time.clock()
#
# print df.head(2)
# print reader[reader['day'] == '20151004']

#
# # 行求和
# df['total'] = df['workertrips'] + df['worker']
# print df.head(n=10)
# # 列求和
# worker_total = df['worker'].sum()
# print worker_total
# # 列求平均
# worker_avg = df['worker'].mean()
# print worker_avg
# 分组
# print df.head(5)
# data = df.groupby('leftXQBH')['worker'].sum()
# with open('xxx.csv', 'w') as f:
#     f.write(DataFrame(data).to_csv())

# print df.count()
#
#
# print 'cost time: %d' % (endtime - startime)
# print 'end'
#
