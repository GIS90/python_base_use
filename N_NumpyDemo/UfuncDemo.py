# -*- coding: utf-8 -*-


import time
import math
import numpy as np

x = [i for i in xrange(1000 * 1000)]
start = time.clock()
for i, t in enumerate(x):
    x[i] = math.sin(t)
print "math.sin:", time.clock() - start

x = [i for i in xrange(1000 * 1000)]
x = np.array(x)
start = time.clock()
np.sin(x, x)
print "numpy.sin:", time.clock() - start

x = np.arange(1, 4)
y = np.arange(2, 5)

print np.add(x, y)
print np.subtract(y, x)
print np.multiply(x, y)
print np.divide(y, x)
print np.true_divide(y, x)
print np.floor_divide(y, x)





