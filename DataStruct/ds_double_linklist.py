# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:
双向链表
主要用node类去记录value，next的值
------------------------------------------------
"""

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/3/17"


class Node(object):
    """
    节点类
    """
    def __init__(self, data, p=0):
        """
        每个节点的初始化
        :param data: 节点的值
        :param p: 节点的位置
        :return: None
        """
        self.data = data
        self.prev = p
        self.next = p


class DuLinkList(object):
    """
    双向链表的类
    """
    def __init__(self):
        self.head = 0

    def initlist(self, datas):
        """
        链表的初始化值
        :param datas: 初始化的值
        :return: None
        """
        self.head = Node(datas[0])

        p = self.head
        for data in datas[1:]:
            node = Node(data)
            p.next = node
            node.prev = p
            p = p.next


    def length(self):
        """
        链表的长度
        :return: length
        """
        p = self.head
        length = 0
        if p == 0:
            return 0
        else:
            while p != 0:
                p = p.next
                length += 1

            return length

    def is_empty(self):
        """
        返回是否是空列表
        :return: True or False
        """
        return True if self.length() == 0 else False

    def clear(self):
        """
        链表的清除
        :return:
        """
        self.head = 0

    def append(self, data):
        """
        链表的追加
        :param data:
        :return:
        """
        node = Node(data)
        if self.head == 0:
            self.head = node
        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = node
            node.prev = p

    def getitem(self, index):
        """
        链表的获取
        :param index: 获取值的位置
        :return: 位置的值
        """
        assert isinstance(index, int)

        if self.is_empty():
            print 'DuLinkList getitem is empty'
            return
        if index < 0 or index > self.length():
            print 'DuLinkList getitem index is error'
            return

        i = 0
        p = self.head
        while p != 0 and i < index:
            p = p.next
            i += 1
        if i == index:
            return p.data

    def insert(self, index, data):
        """
        链表的插入
        :param index: 位置
        :param data: 值
        :return: None
        """
        assert isinstance(index, int)

        if self.is_empty():
            print 'DuLinkList getitem is empty'
            return
        if index < 0 or index > self.length():
            print 'DuLinkList getitem index is error'
            return

        i = 0
        p = self.head
        post = self.head
        node = Node(data)

        while i < index and p != 0:
            post = p
            p = p.next
            i += 1
        if i == index:
            post.next = node
            node.next = p
            node.prev = post
            p.prev = node

    def delete(self, index):
        """
        链表的删除
        :param index:
        :return:
        """
        assert isinstance(index, int)

        if self.is_empty():
            print 'DuLinkList getitem is empty'
            return
        if index < 0 or index > self.length():
            print 'DuLinkList getitem index is error'
            return

        i = 0
        post = self.head
        p = self.head

        while p != 0 and i < index:
            post = p
            p = p.next
            i += 1
        if i == index:
            post.next = p.next
            p.next.prev = post





