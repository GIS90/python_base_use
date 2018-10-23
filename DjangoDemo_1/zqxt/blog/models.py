from __future__ import unicode_literals
from django.db import models
from django.utils.encoding import python_2_unicode_compatible


# Create your models here.
@python_2_unicode_compatible
class Author(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    qq = models.CharField(max_length=12)
    addr = models.TextField()
    email = models.EmailField()

    def __str__(self):
        return self.name

    def __unicode__(self):
        self.__str__()


@python_2_unicode_compatible
class Article(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author)
    content = models.TextField()
    score = models.IntegerField()
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.title

    def __unicode__(self):
        self.__str__()


@python_2_unicode_compatible
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def __unicode__(self):
        self.__str__()
