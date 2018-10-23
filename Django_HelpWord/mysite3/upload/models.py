# -*- coding: utf-8 -*-


from django.db import models


class UploadFileInfo(models.Model):
    user = models.CharField(max_length=40)
    ip = models.CharField(max_length=40)
    loadtime = models.DateTimeField(auto_now=True,)
    type = models.CharField(max_length=10)
    path = models.FileField()

    # class Meta:
    #     db_table = 'upload_file_informations'

    def __unicode__(self):
        return self.ip + '_' + self.user
