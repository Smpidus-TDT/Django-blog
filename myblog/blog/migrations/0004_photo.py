# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-19 06:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180418_0918'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo_title', models.CharField(default='Photo_title', max_length=32, verbose_name='\u56fe\u7247\u6807\u9898')),
                ('photo_content', models.TextField(null=True, verbose_name='\u56fe\u7247\u5185\u5bb9')),
                ('photo_address', models.CharField(max_length=50, verbose_name='\u56fe\u7247\u5730\u5740')),
            ],
        ),
    ]
