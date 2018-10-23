# -*- coding: utf-8 -*-

"""
------------------------------------------------
describe: 
------------------------------------------------
"""
from __future__ import unicode_literals
import random
from zqxt.wsgi import *
from blog.models import *


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/27"


author_names = ['WeizhongTu1', 'twz9151', 'dachui1', 'zhe1', 'zhen1']
article_titles = ['Django 教程', 'Python 教程', 'HTML 教程']


def create_authors():

    for name in author_names:
        print 'author: %s' % name
        author, created = Author.objects.get_or_create(name=name)
        author.qq = ''.join(str(random.choice(range(10))) for _ in range(8, 12))
        author.age = random.randint(1, 200)
        author.email = '%s@163.com' % name
        author.addr = 'addr_%s' % random.randrange(1, 3)
        author.save()


def create_articles_and_tags():

    for article_title in article_titles:
        tag_name = article_title.split(' ', 1)[0]
        tag, created = Tag.objects.get_or_create(name=tag_name)
        arcicle_author = random.choice(Author.objects.all())

        for i in range(1, 21, 1):
            title = '%s_%s' % (article_title, i)
            print 'title: %s' % title
            arcicle, created = Article.objects.get_or_create(
                title=title,
                defaults={
                    'author': arcicle_author,
                    'content': '%s 正文' % title,
                    'score': random.randint(1, 100),
                }
            )
            arcicle.tags.add(tag)


def main():
    create_authors()
    # create_articles_and_tags()


if __name__ == '__main__':
    main()






