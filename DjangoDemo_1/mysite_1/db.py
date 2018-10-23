# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
import os
import django
from blog.models import *
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")


print django.VERSION
if django.VERSION >= (1, 7):
    django.setup()


with open('blog.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        title, content = line.split('****')
        Blog.objects.create(title=title, content=content)
        print line







