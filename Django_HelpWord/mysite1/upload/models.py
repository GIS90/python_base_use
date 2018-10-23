# coding: utf-8

from django.db import models

# Create your models here.


class FileInfo(models.Model):
    user = models.CharField(u'所有者', max_length=40)
    ip = models.CharField(u'Ip地址', max_length=40)
    path = models.FileField(u'位置', upload_to='/upload/file/')

    class Meta:
        db_table = 'upload_file_info'

    def __unicode__(self):
        return self.ip + '_' + self.user
