# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""


# import inspect
#
#
# for attr, value in inspect.getmembers(object):
#     print attr, value
#
# print '----------------------------'
# for attr, value in vars(object).iteritems():
#     print attr, value
#
#
# print '-' * 20
# print dir(object)

# object.__dict__只读


# class C(object):
#     def foo(self):
#         pass
#
# print C.foo
# print C().foo
#
#
# print C.__dict__['foo'].__get__(C(), C)
class A():
    const = 1

    def __init__(self):
        print 'A __init__'

    def __new__(cls, *args, **kwargs):
        print 'A __new__'

    def __doc__(self):
        print 'A __doc__'

    def foo(self):
        pass

    def __class__(self):
        pass


a, b = list('123'), list('234')
c = zip(a, b)
d = zip(*c)


# print c, d

# __metaclass__ = upper_attr


def upper_attr(class_name, class_parents, class_attrs):
    attrs = ((name, value) for name, value in class_attrs if not name.startswith('__'))

    upper_attrs = dict((name.upper(), value) for name, value in attrs)

    return upper_attrs


from functools import reduce
from itertools import chain

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"d": 4, "e": 5, "f": 6}
my_list = [dict1, dict2]

a = 'abc'
print unicode(a, "utf-8")
