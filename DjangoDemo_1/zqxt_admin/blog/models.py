from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    pubtime = models.DateTimeField(auto_now_add=True, editable=True)
    updtime = models.DateTimeField(auto_now_add=True, editable=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.title


class Person(models.Model):
    fname = models.CharField(max_length=20)
    lname = models.CharField(max_length=30)

    def myname(self):
        return self.fname + self.lname

    fullname = property(myname)
