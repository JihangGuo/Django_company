# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 03:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edit', '0008_auto_20170714_1641'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='projects_url1',
            field=models.FileField(blank=True, upload_to='projects_pic/'),
        ),
        migrations.AddField(
            model_name='projects',
            name='projects_url2',
            field=models.FileField(blank=True, upload_to='projects_pic/'),
        ),
        migrations.AddField(
            model_name='projects',
            name='projects_url3',
            field=models.FileField(blank=True, upload_to='projects_pic/'),
        ),
        migrations.AddField(
            model_name='projects',
            name='projects_url4',
            field=models.FileField(blank=True, upload_to='projects_pic/'),
        ),
    ]
