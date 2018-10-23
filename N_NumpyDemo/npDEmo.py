#coding:utf-8



import numpy as np



a = np.arange(0, 60, 10).reshape(-1, 1)

print a
print a.shape



b = np.arange(0, 5).reshape(1,-1)
print b
print b.shape

print a+b

print b.repeat(10,axis=0)






