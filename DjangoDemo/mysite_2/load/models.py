from django.db import models

# Create your models here.


class User(models.Model):
    username = models.CharField(max_length=20)
    loadfile = models.FileField(upload_to='./file/')

    def __unicode__(self):
        return self.username
