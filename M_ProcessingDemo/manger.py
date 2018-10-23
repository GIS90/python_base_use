# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""


class Cls(object):
    def __init__(self):
        self.__x = None

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @x.deleter
    def x(self):
        del self.__x


if __name__ == '__main__':
    c = Cls()
    c.x = 100
    y = c.x
    print("set & get y: %d" % y)

    del c.x
    print("del c.x & y: %d" % y)


def deco(arg):
    def _deco(func):
        def __deco():
            print("before %s called [%s]." % (func.__name__, arg))
            func()
            print("  after %s called [%s]." % (func.__name__, arg))

        return __deco

    return _deco


@deco("mymodule")
def myfunc():
    print(" myfunc() called.")


@deco("module2")
def myfunc2():
    print(" myfunc2() called.")


class echo:
    def __enter__(self):
        print 'enter'

    def __exit__(self, *args):
        print 'exit'


with echo() as e:
    print 'echo'


def func():
    for i in xrange(10):
        yield i

for i in func():
    print i
    


l = [x for x in range(20)]
print l
