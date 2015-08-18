# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0002_petrelation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='petRelation',
            field=models.ForeignKey(to='advert.PetRelation'),
        ),
    ]
