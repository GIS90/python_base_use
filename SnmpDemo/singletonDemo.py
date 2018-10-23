#coding:utf-8




class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'_instance'):
            cls._instance=super(Singleton,cls).__new__(cls)
        return cls._instance

class MyClass(Singleton):
    a=1

class Singleton1(object):
    _instance={}
    def __new__(cls, *args, **kwargs):
        ob=super(Singleton1,cls).__new__(cls, *args, **kwargs)
        ob.__dict__=cls._instance
        return ob



class singletonDemo(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(singletonDemo,'_instance'):
            cls._instance=super(singletonDemo,cls).__new__(cls)
        return cls._instance
class singleDemo1(object):
    _instance={}
    def __new__(cls, *args, **kwargs):
        ob=super(singleDemo1,cls).__new__(cls)
        ob.__dict__=cls._instance
        return ob

