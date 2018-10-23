# -*- coding: utf-8 -*-

import numpy as np


c = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]])


d = c.reshape(4, 3)
# print d
#
# print np.arange(1, 100, 2, dtype=int)
# print np.linspace(1, 10, 100)
# print np.logspace(1, 10, 20)

s = 'asdfghjkl'
print np.fromstring(s, dtype=np.int8, count=-1, sep='')
ss = np.array([97,  98,  99, 100, 101, 102, 103, 104], dtype=np.int8)
print np.fromstring(ss, dtype=np.int64)


def funa(x, y, n=1):
    return (x + 1) * (y + 1) * n

fa = np.fromfunction(funa, (9, 9), dtype=int)
print fa


x = np.random.rand(10)
print x
print x > 0.5
print x[x > 0.5]

arr = np.arange(0, 60, 10).reshape(-1, 1) + np.arange(0, 6)
print arr

persontype = np.dtype({
    'names': ['name', 'age', 'weight'],
    'formats': ['S32', 'i', 'f']})
a = np.array([("Zhang", 32, 75.5), ("Wang", 24, 65.2)], dtype=persontype)
a[0]['name'] = 'hml'
print a
print a.strides
print a.dtype
print a[:]['age']
print a.tofile('test.bin')



