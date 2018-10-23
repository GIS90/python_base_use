# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: demo.py
@time: 2016/8/16 16:11
@describe: 
@remark: 
------------------------------------------------
"""
from PIL import Image
import os
import sys


def show_pic(infile):
    im = Image.open(infile)
    print "Image format: %s" % im.format
    print "Image size: %s" % str(im.size)
    print "Image mode: %s" % im.mode
    im.show()


def transfer_pic_format_jpg(infile):
    f, _ = os.path.splitext(infile)
    outfile = f + "png"
    if infile != outfile:
        try:
            Image.open(infile).save(outfile)
            print "%s tranfer success" % f
        except IOError:
            print "%s tranfer failure" % f


if __name__ == "__main__":
    infile = "mebk.jpg"
    show_pic(infile)


