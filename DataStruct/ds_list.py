# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
列表
------------------------------------------------
"""


l = []
l.append(3)
l.extend([12, 4, 6])
l.insert(1, 'hello')
l.remove(3)


mat = [
        [1,2,3],
        [4,5,6],
        [7,8,9]
        ]

# print ([[row[i] for row in mat] for i in [0,1,2]])
print list(zip(mat))
print list(zip(*mat))




