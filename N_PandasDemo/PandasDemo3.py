# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import numpy as np
import pandas as pd

dates = pd.date_range('20170101', periods=6)
# print dates

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
# print df

# # 基本操作
# print df.dtypes
# print df.head(n=2)
# print df.tail(n=3)
# print df.index
# print df.columns
# print df.describe()

# # 3 选择
# print df['A']
# print df[0:3]
# print df.loc[dates[0]]
# print df.loc['20170103', ['B', "C"]]
# print df.iloc[2:3, 3:]

# 4 缺失值处理
# df1 = df.reindex(index=dates[0:4], columns=list(df.columns) + ['E'])
# df1.loc[dates[0]:dates[1], "E"] = 1
# print df1
# print df1.fillna(value=100)
# print df1.dropna(how='any')
# print pd.isnull(df1)


# # 5相关操作
#
# # print df.mean(1)
#
# # s = pd.Series([1, 2, 4, np.nan, 45, 6], index=dates).shift(2)
# s = pd.Series(np.random.randint(1, 9, size=10))
# print s
# print s.value_counts()
#

# 6合并

# 7 分组
df = pd.DataFrame({
    'A': ['foo', 'far', 'foo', 'far', 'foo', 'far'],
    'B': ['one', 'two', 'one', 'two', 'one', 'two'],
    'C': np.random.randn(6),
    'D': np.random.randn(6)
})
print df