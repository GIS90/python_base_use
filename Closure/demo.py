# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""

#
# def func(name):
#     def inner_func(age):
#         print '%s age is %d' % (name, age)
#     return inner_func
#
# a = func('Tom')
# print a(24)

#
# def outer(x):
#     y = [1, 2, 3]
#     def inner(z):
#         print x
#         print y
#         print z
#         print locals()
#
#     return inner
#
# f = outer(5)
# print callable(f)
# print f(10)

# import logging
#
#
# def usr_log(func):
#
#     def wrapper(*args, **kwargs):
#         logging.info('%s is running' % func.__name__)
#         return func(*args, **kwargs)
#
#     return wrapper
#
#
# def a_foo():
#     print 'a_foo'
#     return 'a'
#
#
# @usr_log
# def b_foo():
#     print 'b_foo'
#     return 'b'
#
#
# a = usr_log(a_foo)
# print a()
#
# print b_foo()
#
#
import logging


def usr_log(func):

    def wrapper(*args, **kwargs):
        print 'wrapper'
        logging.warning('%s is running' % func.__name__)
        return func(*args, **kwargs)

    return wrapper


@usr_log
def foo():
    print 'foo'


print foo
print foo()

