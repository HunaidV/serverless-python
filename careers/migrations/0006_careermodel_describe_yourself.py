# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-05 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('careers', '0005_careermodel_linkedin_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='careermodel',
            name='Describe_yourself',
            field=models.TextField(default='', max_length=5000),
        ),
    ]