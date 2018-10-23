from django.db import models


# Create your models here.


class File(models.Model):
    user = models.CharField(max_length=40)
    ip = models.CharField(max_length=40)
    file = models.FileField(upload_to='/upload_files/')

    class Meta:
        db_table = 'file'

    def __unicode__(self):
        return self.ip + '_' + self.user
