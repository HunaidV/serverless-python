# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-19 07:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0006_blogmodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d/'),
        ),
    ]
