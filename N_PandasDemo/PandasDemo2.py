# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from pandas import Series
from pandas import DataFrame

# Series
# s = Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])
# print s
# print s['a']
# s['c'] = 8
# print s
# print s.index
# print s.values

# DataFrame

d = {"name": ["Haha", "Hehe", "Xixi"], "age": [20, 22, 25]}

df = DataFrame(d, columns=["name", "age", "hight"])
print df

