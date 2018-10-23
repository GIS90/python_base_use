# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import numpy as np
import pandas as pd

from pandas import Series
from pandas import DataFrame


SIZE = 100 * 100

flag = True
chunks = []
sordata = r'E:\\data\XY\test.csv'

# reader = pd.read_csv(sordata, iterator=True)
# while flag:
#     try:
#         chunk = reader.get_chunk(SIZE)
#         chunks.append(chunk)
#     except StopIteration:
#         flag = False
#         print 'Iterator is stop'
#
# df = pd.concat(chunks, ignore_index=True)
#
# print df['passenger_count'] + df['trip_time_in_secs']

seq = list("asdfghjk")
print seq
print seq[:-2]
print seq[::-1]
