#coding:utf-8



import yaml


yamlFile=r'D:\Py_File\YamlDemo\dev_192.168.3.21.yaml'
content=yaml.load(file(yamlFile))
print content['database']['type']
print len(content)