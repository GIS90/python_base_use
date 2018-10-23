# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: 1.0v
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: df.py
@time: 2016/10/26 22:20
@describe: 
@remark: 
------------------------------------------------
"""

import pandas as pd
import numpy as np


wthfood = pd.DataFrame({"Date": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
                        "Weather": ["cold", "hot", "hot", "cold", "hot", "cold", "cold"],
                        "Food": ["soup", "ice", "soup", "banana", "banana", "soup", "soup"],
                        "Price": 10 * np.random.rand(7)})
print wthfood[1:4]
print "Concat:"
print pd.concat([wthfood[0:3], wthfood[5:]])
print "Append:"
print wthfood[1:3].append(wthfood[5:])

