# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.CharField(max_length=40)),
                ('ip', models.CharField(max_length=40)),
                ('file', models.FileField(upload_to=b'/upload_files/')),
            ],
            options={
                'db_table': 'file',
            },
        ),
    ]
