# -*- coding: utf-8 -*-


from pandas import DataFrame

# s = Series([2, 4, 5, 8], index=['a', 'b', 'c', 'd'])
# print s
# print s.values
# print s.index

data = {'state': ['Ohino', 'Ohino', 'Ohino', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = DataFrame(data, index=['one', 'two', 'three', 'four', 'five'], columns=['year', 'state', 'pop', 'debt'])

# print df
# print df.index
# print df.columns
# print df.dtypes
# print df.shape
# print len(df)
print df.iloc[1:2, 2:3]
print df.describe()
