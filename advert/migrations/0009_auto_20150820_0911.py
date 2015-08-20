# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.files.storage


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0008_auto_20150820_0835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='petImage',
            field=models.ImageField(null=True, upload_to='pets', storage=django.core.files.storage.FileSystemStorage(location='public/media'), blank=True),
        ),
    ]
