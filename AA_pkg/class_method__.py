# -*- coding: utf-8 -*-

"""
------------------------------------------------
@version: ??
@author: PyGoHU
@contact: gaoming971366@163.com
@software: PyCharm Community Edition
@file: class_method__.py
@time: 2016/8/14 10:34
@describe: 
@remark: 
------------------------------------------------
"""


class Inst(object):
    def __init__(self, par):
        self.par = par
    def __eq__(self, other):
        return self.par == other
    def __ne__(self, other):
        return self.par != other


if __name__ == '__main__':
    pass

