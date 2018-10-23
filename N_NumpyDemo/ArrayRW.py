# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/3/29'
"""
#
# import numpy as np
#
#
# a = np.arange(0, 12).reshape(3, 4)
# print a
# np.save('a.npy', a)
# c = np.load('a.npy')
#
# a = np.arange(0, 12, 0.5).reshape(4, -1)
# print a
# np.savetxt("a.txt", a, fmt='%d', delimiter=',')
# print np.loadtxt("a.txt", delimiter=',')



import numpy as np


# n = np.arange(60, dtype="f").reshape(2, 5, 6)
# print n.ravel()
# print n.flatten().reshape(3, 4, 5).transpose()



a = np.arange(12).reshape(3, 4)
b = 2 * a
c = np.arange(2)
d = 2 * c
# print np.hstack((a, b))
# print np.vstack((a, b))
# print np.concatenate((a, b))
# print np.column_stack((c, d))
# print np.row_stack((c, d))
# print np.dstack((a, b))

a = np.arange(27).reshape(3, 3, 3)
# print a
# print np.hsplit(a, 3)
# print np.vsplit(a, 3)
# print np.dsplit(a, 3)

print a.ndim
print d.itemsize
print d.tostring()
print d.nbytes
print d.T
print d.flat
print d.tolist()
