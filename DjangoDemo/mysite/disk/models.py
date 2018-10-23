from django.db import models


# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=40)
    headimg = models.FileField(upload_to='./upload')

    def __unicode__(self):
        return self.username

    def __str__(self):
        return self.username
