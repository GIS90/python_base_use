# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
#
# import os
#
# print [d for d in os.listdir("E:")]
# print [x for x in range(1, 10)]
# print [x for x in range(1, 20) if x % 2 == 0]
# print [m + n for m in range(1, 20) for n in range(2, 40)]
#
# L = ['Hello', 'World', 18, 'Apple', None]
# print [s.lower() for s in L if isinstance(s, basestring)]
#
# from collections import Iterator
#
# print isinstance([1, 32], Iterator)
#
# s = list(map(str, [range(20)]))
# print s

#
# def log(func):
#     def wrapper(*args, **kw):
#         print('call %s():' % func.__name__)
#         return func(*args, **kw)
#     return wrapper
#
#
# @log
# def now():
#     print('2015-3-25')
#
#
# now()

#
# def logger(text):
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             print('%s %s():' % (text, func.__name__))
#             return func(*args, **kw)
#
#         return wrapper
#
#     return decorator
#
#
# @logger('DEBUG')
# def today():
#     print('2015-3-25')


# today()
# print(today.__name__)
import sys

print sys.path


class Student(object):
    def __int__(self, name):
        self.__name = name

    def show(self):
        print self.__name





class Student(object):
    __slots__ = ('name', 'age')  # 用tuple定义允许绑定的属性名称

    def __init__(self):
        self.name


class GraduateStudent(Student):
    pass


s = Student()  # 创建新的实例
s.name = 'Michael'  # 绑定属性'name'
s.age = 25  # 绑定属性'age'
# ERROR: AttributeError: 'Student' object has no attribute 'score'
print hasattr(s, 'name')
try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

g = GraduateStudent()
g.score = 99
print('g.score =', g.score)
