# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-02-17 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogging', '0004_blogmodel_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogmodel',
            name='content',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]