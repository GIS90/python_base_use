# coding:utf-8



dishes = {'eggs': 2, 'sausage': 1, 'bacon': 1, 'spam': 500}
keys = dishes.viewkeys()
values = dishes.viewvalues()

print keys
print values
del dishes['spam']

k = dishes.keys()
v = dishes.values()
i = dishes.items()
print k
print v
print i
