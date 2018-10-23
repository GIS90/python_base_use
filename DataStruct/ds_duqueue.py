# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
双向队列
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/19"


class DuQueue(object):

    def __init__(self, size=100):
        self.dequeue = []
        self.size = size

    def __is_full(self):

        usr_len = len(self.dequeue)
        return True if self.size - usr_len == 0 else False

    def __is_empty(self):

        usr_len = len(self.dequeue)
        return True if self.size - usr_len == self.size else False

    def set_size(self, size):
        assert isinstance(size, int)

        if hasattr(self, 'size'):
            self.size = size
        else:
            raise Exception('Dequeue is not size attr')

    def leftappend(self, item):

        self.dequeue.insert(0, item)

    def rightappend(self, item):

        self.dequeue.append(item)

    def leftdelete(self):

        self.dequeue.pop(0)

    def rightdelete(self):

        self.dequeue.pop()

    def getleft(self):

        return self.dequeue[0]

    def getright(self):

        return self.dequeue[-1]






