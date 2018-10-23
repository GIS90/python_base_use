#coding:utf-8


import yaml


document = """
name: Tom Smith
age: 37
spouse:
    name: Jane Smith
    age: 25
children:
 - name: Jimmy Smith
   age: 15
 - name1: Jenny Smith
   age1: 12
 - name2: J S
   age2: 9
"""
print yaml.load(document)

stream=open('document.yaml','w')
print yaml.dump(yaml.load(document),stream)




s1='中文'
s2=u'中文'
print s1
print type(s1.decode('utf-8'))
print s2
print type(s2)













