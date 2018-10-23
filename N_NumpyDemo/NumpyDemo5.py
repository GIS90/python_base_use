# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import numpy as np

# array创建
# arr = np.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]], dtype=np.complex)
# print arr.shape
# print arr.dtype
# arr_new = arr.reshape(2, -1)
# print arr
# print arr_new

# 内建函数创建
# ar = np.arange(0, 2, 0.2)
# print ar
# al = np.linspace(1, 10, 15)
# print al
# alg = np.logspace(1, 2, 20)
# print alg

# 函数创建

# def func(n, m):
#     return (n + 1) * (m + 1)
#
#
# arr = np.fromfunction(func, (9, 9))
# print arr
#
# arr = np.random.rand(10)
# print arr[arr > 0.5]

# persontype = np.dtype({
#     'names': ['name', 'age', 'weight'],
#     'formats': ['S32', 'i', 'f']})
#
# a = np.array([("Zhang", 32, 75.5), ("Wang", 24, 65.2)], dtype=persontype)
# print a
import time
import math


x = [i * 0.001 for i in xrange(1000 * 1000)]
start = time.clock()
for index, value in enumerate(x):
    x[index] = math.sin(value)
print "math.sin:", time.clock() - start

x = [i * 0.001 for i in xrange(1000 * 1000)]
x = np.array(x)
start = time.clock()
for index, value in enumerate(x):
    x[index] = np.sin(value)
print "numpy.sin:", time.clock() - start



