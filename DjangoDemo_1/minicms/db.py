# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
from minicms.wsgi import *
from news.models import Column, Article

print 'start'
columns = [
    ('体育新闻', 'sports'),
    ('社会新闻', 'society'),
    ('科技新闻', 'tech'),
]
for column_name, column_url in columns:
    print column_name
    c = Column.objects.get_or_create(name=column_name, slug=column_url)[0]

    for i in range(10):
        article = Article.objects.get_or_create(
                title='{%s}_{%s}' % (column_name, i),
                slug='article_%s' % i,
                content='新闻的详细内容：%s %s' % (column_name, i)
        )[0]
        article.column.add(c)

print 'end'
