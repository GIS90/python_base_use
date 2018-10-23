# coding:utf-8

import numpy
import os


a = numpy.array([1, 2, 3, 4])
b = numpy.array((5, 6, 7, 8))
c = numpy.array([[1, 2, 3, 4], [4, 5, 6, 7], [7, 8, 9, 10]], dtype=complex)

s = "abcdefgh"

print numpy.fromstring(s, dtype=numpy.int8)
print numpy.fromstring(s, dtype=numpy.int32)
print numpy.fromstring(s, dtype=numpy.int16)
