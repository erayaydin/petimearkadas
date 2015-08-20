# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0005_auto_20150818_1325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='petSex',
            field=models.BooleanField(default=0, choices=[(0, 'Erkek'), (1, 'Dişi')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='petSick',
            field=models.BooleanField(default=0, choices=[(0, 'Sağlıklı'), (1, 'Hasta')]),
        ),
    ]
