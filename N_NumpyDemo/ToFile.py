# -*- coding: utf-8 -*-

import numpy as np
a = np.arange(0, 12).reshape(3, 4)
print a
a.tofile('a.bin')
print a.dtype
print '-------------------------------------------------'
b = np.fromfile('a.bin', dtype=a.dtype).reshape(3, 4)
print b



