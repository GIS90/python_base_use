# -*- coding: utf-8 -*-

# """
# ------------------------------------------------
# describe:
# 用python去实现单向链表
# 主要用node类去记录value，next的值
# ------------------------------------------------
# """
#
# __version__ = "v.10"
# __author__ = "PyGo"
# __time__ = "2017/3/17"
#
#
# class Node(object):
#     """
#     节点类
#     """
#
#     def __init__(self, data, p=0):
#         """
#         初始化
#         :param data: 节点的值
#         :param p: 节点的指向，默认为0，代表结束
#         :return: None
#         """
#         self.data = data
#         self.next = p
#
#
# class LinkList(object):
#     """
#     单向链表类
#     """
#
#     def __init__(self):
#         """
#         链表类初始化
#         :return: None
#         """
#         self.head = 0
#
#     def initlist(self, datas):
#         """
#         定义好的链表进行初始化赋值
#         :param datas:
#         :return: None
#         """
#         self.head = Node(datas[0])
#         p = self.head
#         for data in datas[1:]:
#             node = Node(data)
#             p.next = node
#             p = p.next
#
#     def length(self):
#         """
#         获取链表对象的长度
#         :return: 链表的长度length
#         """
#         p = self.head
#         length = 0
#         if p == 0:
#             return 0
#         else:
#             while p != 0:
#                 length += 1
#                 p = p.next
#
#             return length
#
#     def is_empty(self):
#         """
#         判断链表是否为空
#         :return: True or False
#         """
#         return True if self.length() == 0 else False
#
#     def clear(self):
#         self.head = 0
#
#     def getitem(self, index):
#         """
#         链表的索引值获取
#         :param index: 索引值
#         :return: 索引值的value值返回
#         """
#         assert isinstance(index, int)
#
#         if self.is_empty():
#             print 'linklist is empty'
#             return
#         elif index < 0 or index > self.length():
#             print 'linklist insert index is error'
#             return
#
#         i = 0
#         p = self.head
#         while p != 0 and i < index:
#             p = p.next
#             i += 1
#         if i == index:
#             return p.data
#
#     def append(self, data):
#         """
#         链表的追加
#         :param data: 追加的对象值，因为追加都是末尾追加
#         :return: None
#         """
#         node = Node(data)
#         if self.head == 0:
#             self.head = node
#         else:
#             p = self.head
#             while p != 0:
#                 p = p.next
#             p.next = node
#
#     def insert(self, index, data):
#         """
#         链表的插入，选定位置，如果非选定位置，默认添加到末尾
#         :param index: 插入的位置
#         :param data: 插入的数值
#         :return: None
#         """
#         assert isinstance(index, int)
#
#         if self.is_empty():
#             print 'linklist is empty'
#             return
#         elif index < 0 or index > self.length():
#             print 'linklist insert index is error'
#             return
#
#         node = Node(data)
#         post = self.head
#         p = self.head
#         i = 0
#         while p != 0 and i < index:
#             post = p
#             p = p.next
#             i += 1
#         if i == index:
#             post.next = node
#             node.next = p
#
#     def delete(self, index):
#         """
#         删除指定位置上的节点
#         :param index: 位置
#         :return: None
#         """
#         assert isinstance(index, int)
#
#         if self.is_empty():
#             print 'linklist is empty'
#             return
#         elif index < 0 or index > self.length():
#             print 'linklist insert index is error'
#             return
#
#         post = self.head
#         p = self.head
#         i = 0
#         while i < index and p != 0:
#             post = p
#             p = p.next
#             i += 1
#         if i == index:
#             post.next = p.next
#
#     def index(self, data):
#         """
#         链表的值位置查询
#         :param data: 查询的数值
#         :return: 位置
#         """
#         if self.is_empty():
#             print 'linklist is empty'
#             return
#
#         p = self.head
#         i = 0
#         indexes = []
#         while p != 0 and i < self.length():
#             if p.data == data:
#                 indexes.append(i)
#             i += 1
#         return indexes if len(indexes) else -1
#
#
# l = LinkList()
# l.initlist([1, 2, 3, 4, 5, 6])
#
# print l.getitem(5)
# l.insert(5, 10)
# print l.getitem(5)
#
#


class Node(object):
    def __init__(self, value, p=0):
        self.data = value
        self.next = p


class SingleLinkList(object):
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
        if p == 0:
            return 0
        else:
            while p != 0:
                length += 1
                p = p.next

    def append(self, data):
        node = Node(data)

        p = self.head
        if p == 0:
            self.head == node
        else:
            while p != 0:
                p = p.next

            p.next = node

    def insert(self, index, data):

        pass



