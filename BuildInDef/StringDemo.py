#coding:utf-8



strDemo=r'hello \t Python \t !'

print strDemo.capitalize()
print strDemo.center(2,'a')
print strDemo.count('o')
print strDemo.endswith('o')
print strDemo.startswith('h')
print strDemo.expandtabs(1)
print 'Py' in strDemo
print strDemo.index('P')
for i in strDemo:
    print i.isalnum()
    print i.isalpha()
    print i.isdigit()
    print i.isspace()
    print i.istitle()
    print i.islower()
    print i.isupper()
print strDemo.replace('P','PP')
print strDemo.partition('P')[0]
print strDemo.partition('P')[1]
print strDemo.partition('P')[2]
print strDemo.split('P')[1]
print strDemo.splitlines()
print strDemo.swapcase()
print strDemo.title()
print strDemo.translate(None,'oe')
print strDemo.upper()
arrayDemo=[1,2,3,4,5,6,7,8,5,2,10]
arrayDemo.reverse()
print arrayDemo
arrayDemo.sort()
print arrayDemo
