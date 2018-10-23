# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/15'
"""

import pandas as pd
import numpy as np

l = [1, 4, 5, 3, np.nan, 20]
s = pd.Series(l, index=list('abcdef'))
print s
dates = pd.date_range('20160401', periods=6)
print dates
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print df.head(6)
print df.dtypes
print df.tail(1)
print '---------------------------------------------------------------------------------------'
print df.index
print df.values
print df.columns
print '---------------------------------------------------------------------------------------'
print df.describe()
print '---------------------------------------------------------------------------------------'
print df.T
print '---------------------------------------------------------------------------------------'
print df.sort(columns='A')
print '---------------------------------------------------------------------------------------'
print df.sort_index(axis=1, ascending=False)
print '---------------------------------------------------------------------------------------'



