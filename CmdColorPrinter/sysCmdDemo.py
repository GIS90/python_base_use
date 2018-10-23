# - * - coding: utf-8 - * -


class A:
    def __init__(self):
        self.name = 'CeShi'

    @staticmethod
    def getMethod(self):
        print 'Show Method'

a = A()
print getattr(A, 'name', A().name)
print getattr(A, 'age', 'not found')
print getattr(A, 'getMethod', 'not found')
print getattr(A, 'show', 'not found show')
print hasattr(A, 'show')
setattr(A, 'show', 'show')
print hasattr(A, 'show')
print getattr(A, 'show', 'not found show')
print dir(A)
print A.__dict__
print A.__doc__
print A.__module__