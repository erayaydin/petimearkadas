# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0004_profile_petsex'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advert',
            name='user',
        ),
        migrations.AddField(
            model_name='advert',
            name='profile',
            field=models.ForeignKey(default=None, to='advert.Profile'),
            preserve_default=False,
        ),
    ]
