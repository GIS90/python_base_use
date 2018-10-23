# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
python实现stack堆栈
先进先出的原则
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/17"


STACK_SIZE = 100


class Stack(object):
    """
    堆栈类，实现先进后出的数据结构
    """

    def __init__(self, size=STACK_SIZE):

        self.size = size
        self.stack = []

    def push(self, item):
        if not self._is_full():
            self.stack.append(item)
        else:
            raise Exception("Stack is full, overflow")

    def pop(self, item):
        if not self._is_empty():
            self.stack.pop()
        else:
            raise Exception("Stack is full, expty")
    def _is_full(self):
        usr_size = len(self.stack)
        return True if self.size - usr_size == 0 else False

    def _is_empty(self):
        usr_size = len(self.stack)
        return True if self.size - usr_size == self.size else False



