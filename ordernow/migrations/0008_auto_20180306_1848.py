# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-06 13:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordernow', '0007_auto_20180304_0026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='Related_to',
            field=models.CharField(choices=[('contentwriting', 'Content Writing'), ('webdevelopment', 'Web Development'), ('graphicsdesigning', ' Graphics Designing'), ('interiorsdesigning', ' Interior Designing'), ('Assignment Writing', 'Assignment Writing')], default=' ', max_length=35),
        ),
    ]
