# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 18:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bottom_ninth', '0003_auto_20171204_1202'),
    ]

    operations = [
        migrations.AlterField(
            model_name='batter',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
