# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-20 08:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20180420_1633'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='CreateTime',
        ),
    ]
