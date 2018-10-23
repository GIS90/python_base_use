# -*- coding: utf-8 -*-

import numpy as np

a = np.arange(0, 60, 10).reshape(-1, 1)
print a.shape

b = np.arange(0, 5, 1)
print b.shape


x, y = np.ogrid[0:5, 0:5]
print x
print y

a = np.arange(12).reshape(2, 3, 2)
b = np.arange(12, 24).reshape(2, 2, 3)
print a
print b
print np.dot(a, b)




