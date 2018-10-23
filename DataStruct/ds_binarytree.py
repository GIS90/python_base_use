# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
二叉树的类实现

------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/18"


class BinaryTree(object):
    """
    二叉树的类
    """
    def __init__(self, item):
        self.item = item
        self.leftchild = None
        self.rightchild = None

    def insertleft(self, item):

        if self.leftchild is None:
            self.leftchild = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.leftchild = self.leftchild
            self.leftchild = t

    def rightchild(self, item):

        if self.rightchild is None:
            self.rightchild = BinaryTree(item)
        else:
            t = BinaryTree(item)
            t.rightchild = self.rightchild
            self.rightchild = t








