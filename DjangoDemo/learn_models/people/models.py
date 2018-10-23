from django.db import models

# Create your models here.


class Persopn(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name

