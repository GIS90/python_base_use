from django.db import models

# Create your models here.


class Lead(models.Model):
    name = models.CharField(max_length=256)
    gender = models.CharField(max_length=2)
    languages = models.CharField(max_length=256)
    cardnum = models.CharField(max_length=20)
    exdate = models.DateTimeField()
    profess = models.BooleanField()
