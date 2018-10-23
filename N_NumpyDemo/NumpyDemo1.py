# -*- coding: utf-8 -*-


import numpy as np


print np.version.version

a = np.array([1, 2, 3, 4])
b = np.array((5, 6, 7, 8))
c = np.array([[1, 2, 3, 4],[4, 5, 6, 7], [7, 8, 9, 10]])

print a
print b
print c

print a.shape, c.shape

d = a.reshape(2, 2)
print d
a[0] =100
print d

e = np.array(d, dtype=complex)
print e

print np.arange(1, 100, 2, dtype=float)
print np.linspace(1, 10, 100)
print np.logspace(1, 10, 20)

def func(i, j):
    return i % 4 + 1
print np.fromfunction(func, (10, 2))






