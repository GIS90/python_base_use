# coding: utf-8

#
# class MyDict(object):
#     def __init__(self):
#         print'call fun __init__'
#
#         self.item = {}
#
#     def __getitem__(self, key):
#         print'call fun __getItem__'
#
#         return self.item.get(key)
#
#     def __setitem__(self, key, value):
#         print'call fun __setItem__'
#
#         self.item[key] = value
#
#     def __delitem__(self, key):
#         print'cal fun __delitem__'
#
#         del self.item[key]
#
#     def __len__(self):
#         return len(self.item)
#
#
# mydict = MyDict()
# print mydict.item
#
# mydict[2] = 'China'
# print mydict[2]
# del mydict[2]
#
# print mydict.item
#
# print len(mydict)


class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        print self.name
        print self.gender

    def __call__(self, friend):
        print 'My name is %s...' % self.name
        print 'My friend is %s...' % friend

p = Person('Jam', 'Male')
print p('Tom')


