# coding: utf-8


from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible
# Create your models here.


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(u'标题', max_length=100)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发布时间', auto_now_add=True, editable=True)
    update_time = models.DateTimeField(u'更新时间', auto_now=True, null=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def my_prooperty(self):
        return self.first_name + self.last_name
    my_prooperty.short_description = 'Full name of person'

    full_name = property(my_prooperty)
