# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0007_profile_petimage'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='petImage',
            field=models.ImageField(blank=True, upload_to='', null=True),
        ),
    ]
