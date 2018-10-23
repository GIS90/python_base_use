# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
    pandas and numpy test demo
    main func is enhance use

i love code, i love python
------------------------------------------------
"""
import numpy as np
import pandas as pd


from pandas import Series
from pandas import DataFrame


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/16"


student = pd.read_csv('lx.csv')

# print student.ix[[1, 2, 5], ['name', 'sex']]
# print student[(student['sex'] == 'm') | (student['height'] > 110)][['name', 'id', 'sex']]


# print student.groupby('sex').mean().sort_values(by = 'id')
#
# pd.merge


print pd.pivot_table(student, values=['height'], columns=['sex'])


