# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UploadFileInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=40)),
                ('ip', models.CharField(max_length=40)),
                ('loadtime', models.DateTimeField(auto_now=True)),
                ('type', models.CharField(max_length=10)),
                ('path', models.FileField(upload_to=b'')),
            ],
        ),
    ]
