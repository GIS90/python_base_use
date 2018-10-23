# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:

------------------------------------------------
"""
import sys

import pandas as pd

reload(sys)
sys.setdefaultencoding('utf8')

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/13"

CHUNK_SIZE = 10 * 10

flag = True
chunks = []
data = 'E:\kakou.csv'

# 设置读取文件的编码，汉字为gbk
reader = pd.read_csv(data, iterator=True, encoding="gbk")
while flag:
    try:
        chunk = reader.get_chunk(CHUNK_SIZE)
        chunks.append(chunk)
    except StopIteration:
        flag = False
        print 'Iterator is stop'

df = pd.concat(chunks, ignore_index=False)

# 处理NA数据
df = df.dropna(how='all')
df = df.fillna(0).drop_duplicates()
# 设置索引
df.set_index('KKID')

print df.loc[(df['KKID'] == 5200212061), ['KKID', 'KKMC', 'JD', 'WD']]



#
# df_use = df[['KKID', 'KKMC', 'JD', 'WD']]
# # 获取values的值
# for value in df_use.values:
#     kkid, kkmc, kkjd, kkwd = value[0], value[1], value[2], value[3]
#     if isinstance(kkmc, unicode):
#         kkmc = kkmc.encode('utf-8')
#
#     print kkid, kkmc, kkjd, kkwd




print 'end'
