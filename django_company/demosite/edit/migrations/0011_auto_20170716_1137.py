# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 03:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edit', '0010_auto_20170716_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='projects_url',
            field=models.FileField(blank=True, null=True, upload_to='projects_pic/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_url1',
            field=models.FileField(blank=True, null=True, upload_to='projects_pic/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_url2',
            field=models.FileField(blank=True, null=True, upload_to='projects_pic/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_url3',
            field=models.FileField(blank=True, null=True, upload_to='projects_pic/'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_url4',
            field=models.FileField(blank=True, null=True, upload_to='projects_pic/'),
        ),
    ]
