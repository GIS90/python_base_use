# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
链表
------------------------------------------------
"""


class Node(object):
    def __init__(self, value, p=0):
        self.data = value
        self.next = p


class LinkList(object):
    def __init__(self):
        self.head = 0

    def initlist(self, datas):
        self.head = Node(datas[0])

        p = self.head
        for data in datas[1:]:
            node = Node(data)
            p.next = node
            p = p.next

    def length(self):

        p = self.head
        length = 0
        while p != 0:
            length += 1
            p = p.next
        return length

    def is_empty(self):

        return True if self.length() == 0 else False

    def clear(self):
        self.head = 0

    def append(self, data):

        q = Node(data)
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p != 0:
                p = p.next
            p.next = q

    def getitem(self, index):
        assert isinstance(index, int)

        if self.is_empty():
            print 'linklist is empty'
            return
        elif index < 0 or index > self.length():
            print 'getitem index is error'
            return

        i = 0
        p = self.head
        while p.next != 0 and i <= index:
            p = p.next
            i += 1
            if i == index:
                return p.data

    def insert(self, index, data):
        assert isinstance(index, int)

        if index < 0 or index > self.length():
            print 'getitem index is error'
            return
        if index == 0:
            q = Node(data)
            self.head = q

        p = self.head
        post = self.head
        i = 0
        while p.next != 0 and i < index:
            post = p
            p = p.next
            i += 1

            if index == i:
                q = Node(data, p)
                post.next = q
                q.next = p
                break

    def delete(self, index):
        assert isinstance(index, int)

        if self.is_empty():
            print 'linklist is empty'
            return
        elif index < 0 or index > self.length():
            print 'delete index is error'
            return

        post = self.head
        p = self.head
        i = 0
        while p.next != 0 and i < index:
            post = p
            p = p.next
            i += 1

            if i == index:
                post.next = p.next
                break



