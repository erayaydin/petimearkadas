# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0006_auto_20150819_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='petImage',
            field=models.ImageField(upload_to='', null=True),
        ),
    ]
