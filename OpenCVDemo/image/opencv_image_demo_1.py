# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
主要学习图像的载入，显示，保存
pygo
------------------------------------------------
"""
import cv2


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/2"


print 'start'

img = cv2.imread('test.jpg', 0)
cv2.imshow('image', img)
key = cv2.waitKey(0) & 0xFF
if key == 27:
    cv2.destroyWindow('image')
elif key == ord('s'):
    cv2.imwrite('testcopy.png', img)
    cv2.destroyAllWindows()







