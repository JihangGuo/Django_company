# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-13 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edit', '0002_auto_20170713_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='details_url',
            field=models.FileField(null=True, upload_to='details_pic/'),
        ),
        migrations.AlterField(
            model_name='glorys',
            name='glorys_url',
            field=models.FileField(null=True, upload_to='glorys_pic/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_url',
            field=models.FileField(null=True, upload_to='news_pic/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_url',
            field=models.FileField(null=True, upload_to='projects_pic/'),
        ),
    ]
