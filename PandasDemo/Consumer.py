# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: Consumer.py
@time: 2016/10/25 14:49
@describe: 
@remark: 
------------------------------------------------
"""

import pandas as pd
from numpy.random import rand
from numpy.random import random_integers

df = pd.DataFrame({"Weather": ["cold", "hot", "cold", "hot", "cold", "hot", "cold"],
                   "Food": ["soup", "ice", "ice", "soup", "ice", "banana", "banana"],
                   "Price": 10 * rand(7)})

print df.shape
# wether = df.groupby("Weather")
# for name, group in wether:
#     print name, group
#
import numpy as np
wf = df.groupby(["Weather", "Food"])
print wf.agg(np.mean)
# for k, v in wf:
#     print k, "----------", v

