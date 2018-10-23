# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/15'
"""
import numpy as np
import pandas as pd

dates = pd.date_range('20160401', periods=6)
print dates
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
print df['B']
print df[0:2]
print '---------------------------------------------------------------------------------------'
print df.loc[dates[0]]
print '---------------------------------------------------------------------------------------'
print df.loc['20160401', ['A', 'B']]
print '---------------------------------------------------------------------------------------'
print df.iloc[0:1, 0:2]
print '---------------------------------------------------------------------------------------'
df2 = df.copy()
df2['E'] = ['one', 'two', 'three', 'four', 'five', 'six']
print df2

print '---------------------------------------------------------------------------------------'
s = pd.Series([1, 2, 3, 4, 5], index=pd.date_range('20160101', periods=5))
print s
print '---------------------------------------------------------------------------------------'
df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
print df1
df1.dropna(how='any')
print df1
d = df1.fillna(value=10)

print '---------------------------------------------------------------------------------------'
print df1.isnull()
print '---------------------------------------------------------------------------------------'
print d.mean(1)


