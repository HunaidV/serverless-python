# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-05 11:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ordernow', '0009_remove_ordermodel_have_a_budget'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordermodel',
            name='email',
            field=models.TextField(default='', max_length=254),
        ),
    ]