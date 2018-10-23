# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
from models import Blog, Author

# b = Blog(name='Beat Blog', tagline='all the latest news')
# b.save()

Author.objects.create(name='Zhangsan', email='zhangsan@163.com')

author = Author(name='Lisi', email='lisi@126.com')
author.save()

Author.objects.get_or_create(name='Zhuliu', email='zhuliu@126.com')







