# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
python实现队列
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/17"


QUEUE_SIZE = 100


class Queue(object):
    def __init__(self, size=QUEUE_SIZE):
        self.size = size
        self.front = 0
        self.rear = 0
        self.queue = []

    def add(self, item):
        if not self._is_full():
            self.queue[self.rear] = item
            self.rear += 1
        else:
            raise Exception('queue is full')

    def pop(self):
        if not self._is_empty():
            self.front += 1
        else:
            raise Exception('queue is full')

    def _is_full(self):
        usr_size = len(self.queue)
        if self.size - usr_size == 0:
            return True
        else:
            return False

    def _is_empty(self):
        usr_size = len(self.queue)
        if self.size - usr_size == self.size:
            return True
        else:
            return False






