# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-03-02 07:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_auto_20180220_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicemodel',
            name='image',
            field=models.ImageField(null=True, upload_to='service/'),
        ),
    ]