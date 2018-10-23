# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import sys


import random
import pandas as pd
reload(sys)
sys.setdefaultencoding('utf8')


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/9"


points = random.sample(xrange(1, 100), 5)
names = "Haha Hehe Xixi Gaga Wuwu".split()
datas = zip(names, points)

df = pd.DataFrame(datas, columns=['name', 'point'])
df.sort_values(['point'], ascending=False)
print df.head(1)
df.to_csv("E:\\study.csv", index=True)




