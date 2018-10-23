# -*- coding: utf-8 -*-
"""
__author__ = 'Administrator'
__time__ = '2016/4/15'
"""

import Image
import os

curDir = os.path.dirname(__file__)
picName = 'test.jpg'
pic = os.path.abspath(os.path.join(curDir, picName))
im = Image.open(pic)
print im.format
print im.size
print im.mode
box = (100, 100, 200, 200)
region = im.crop(box)
region.save('region.jpg')
ro = region.transpose(Image.ROTATE_180)
ro.save('rotate.jpg')
im.paste(ro, box)
out = im.rotate(30)
out.save('out.jpg')




import ImageEnhance
enhanceer = ImageEnhance.Sharpness(im)
for i in range(8):
    factor = i/4.0
    enhanceer.enhance(factor).save('sharpness%f.jpg' % factor)
