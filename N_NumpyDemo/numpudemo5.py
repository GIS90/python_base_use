# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: numpudemo5.py
@time: 2016/10/21 18:20
@describe: 
@remark: 
------------------------------------------------
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.misc


lena = scipy.misc.lena()
xmax = lena.shape[0]
ymax = lena.shape[1]
xarr = np.arange(xmax)
np.random.shuffle(xarr)
yarr = np.arange(ymax)
np.random.shuffle(yarr)
plt.imshow(lena[np.ix_(xarr, yarr)])
plt.show()


import scipy.misc
import matplotlib.pyplot as plt


lena = scipy.misc.lena()
acopy = lena.copy()
aview = lena.view()
plt.subplot(221)
xmax = lena.shape[0]
ymax = lena.shape[1]
lena[range(xmax), range(ymax)] = 0
plt.imshow(lena)
# plt.subplot(222)
# plt.imshow(acopy)
# plt.subplot(223)
# plt.imshow(aview)
# aview.flat = 0
# plt.subplot(224)
# plt.imshow(aview)
plt.show()
