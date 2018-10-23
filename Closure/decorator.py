# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe:

装饰器的学习
学，就是学

------------------------------------------------
"""
import logging
from functools import wraps

__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/4/18"


# 函数装饰器
# def usr_log(level):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print 'run wrapper'
#             if level == 'warn':
#                 logging.warning('%s is running' % func.__name__)
#             elif level == 'debug':
#                 logging.debug('%s is debug' % func.__name__)
#             return func(*args, **kwargs)
#
#         return wrapper
#     return decorator
#
#
# @usr_log(level='warn')
# def bar():
#     print 'bar is def'
#
# print bar()



# # 类装饰器
#
#
# class Foo(object):
#     def __init__(self, func):
#         self._func = func
#
#     def __call__(self, *args, **kwargs):
#         print 'class decorator is start'
#         print self._func
#         print 'class decorator is end'
#
#
# @Foo
# def bar():
#     print 'bar is def'
#
# bar()
#
# print Foo(1)()


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        print func.__name__ + ' was called'
        return func(*args, **kwargs)
    return with_logging


@logged
def f(x):
    return x * x

print f(10)



