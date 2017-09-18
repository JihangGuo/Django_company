# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-16 07:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edit', '0014_auto_20170716_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='details',
            name='details_text',
            field=models.TextField(default=b'', verbose_name=b'\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x8a\xa8\xe6\x80\x81\xe6\xad\xa3\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='details',
            name='details_time',
            field=models.DateField(auto_now=True, verbose_name=b'\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x8a\xa8\xe6\x80\x81\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='details',
            name='details_title',
            field=models.CharField(max_length=50, verbose_name=b'\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x8a\xa8\xe6\x80\x81\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='details',
            name='details_url',
            field=models.FileField(default=b'', upload_to=b'details_pic/', verbose_name=b'\xe8\xa1\x8c\xe4\xb8\x9a\xe5\x8a\xa8\xe6\x80\x81\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='glorys',
            name='glorys_text',
            field=models.TextField(default=b'', verbose_name=b'\xe5\xa5\x96\xe9\xa1\xb9\xe6\xad\xa3\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='glorys',
            name='glorys_time',
            field=models.DateField(auto_now=True, verbose_name=b'\xe8\x8e\xb7\xe5\xa5\x96\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='glorys',
            name='glorys_title',
            field=models.CharField(max_length=50, verbose_name=b'\xe5\xa5\x96\xe9\xa1\xb9\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='glorys',
            name='glorys_url',
            field=models.FileField(default=b'', upload_to=b'glorys_pic/', verbose_name=b'\xe5\xa5\x96\xe9\xa1\xb9\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='logo_index',
            name='logo_index',
            field=models.FileField(default=b'', upload_to=b'index_logo/', verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8logo\xe5\x9b\xbe'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_text',
            field=models.TextField(default=b'', verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe6\xad\xa3\xe6\x96\x87'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_time',
            field=models.DateField(auto_now=True, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_title',
            field=models.CharField(max_length=50, verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe6\xa0\x87\xe9\xa2\x98'),
        ),
        migrations.AlterField(
            model_name='news',
            name='news_url',
            field=models.FileField(default=b'', upload_to=b'news_pic/', verbose_name=b'\xe6\x96\xb0\xe9\x97\xbb\xe5\x9b\xbe\xe7\x89\x87'),
        ),
        migrations.AlterField(
            model_name='pic_index',
            name='pic_index',
            field=models.FileField(default=b'', upload_to=b'index_pic/', verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe5\xa4\xa7\xe5\x9b\xbe'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_text',
            field=models.TextField(default=b'', verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe8\xaf\xb4\xe6\x98\x8e'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_time',
            field=models.DateField(auto_now=True, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe6\x97\xb6\xe9\x97\xb4'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_title',
            field=models.CharField(max_length=50, verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\x90\x8d\xe7\xa7\xb0'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_type',
            field=models.IntegerField(choices=[(0, '\u516c\u5bd3\u4f4f\u6240/\u9152\u5e97'), (1, '\u5546\u4e1a\u5de5\u7a0b')], verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe7\xb1\xbb\xe5\x9e\x8b'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_url',
            field=models.FileField(default=b'', upload_to=b'projects_pic/', verbose_name=b'\xe9\xa1\xb9\xe7\x9b\xae\xe5\xa4\xa7\xe5\x9b\xbe'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_url1',
            field=models.FileField(default=b'', upload_to=b'projects_pic/', verbose_name=b'\xe7\xbb\x86\xe8\x8a\x82\xe5\xb0\x8f\xe5\x9b\xbe1'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_url2',
            field=models.FileField(default=b'', upload_to=b'projects_pic/', verbose_name=b'\xe7\xbb\x86\xe8\x8a\x82\xe5\xb0\x8f\xe5\x9b\xbe2'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_url3',
            field=models.FileField(default=b'', upload_to=b'projects_pic/', verbose_name=b'\xe7\xbb\x86\xe8\x8a\x82\xe5\xb0\x8f\xe5\x9b\xbe3'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='projects_url4',
            field=models.FileField(default=b'', upload_to=b'projects_pic/', verbose_name=b'\xe7\xbb\x86\xe8\x8a\x82\xe5\xb0\x8f\xe5\x9b\xbe4'),
        ),
        migrations.AlterField(
            model_name='text_index',
            name='about_index',
            field=models.TextField(default=b'', verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe5\x85\xac\xe5\x8f\xb8\xe7\xae\x80\xe4\xbb\x8b'),
        ),
        migrations.AlterField(
            model_name='text_index',
            name='hq_index',
            field=models.FileField(default=b'', upload_to=b'index_text/', verbose_name=b'\xe5\x85\xac\xe5\x8f\xb8\xe5\x9b\xbe\xe7\x89\x87\xef\xbc\x88\xe5\xb0\x8f\xef\xbc\x89'),
        ),
        migrations.AlterField(
            model_name='video_index',
            name='video_index',
            field=models.FileField(default=b'', upload_to=b'index_video/', verbose_name=b'\xe9\xa6\x96\xe9\xa1\xb5\xe5\xae\xa3\xe4\xbc\xa0\xe8\xa7\x86\xe9\xa2\x91'),
        ),
    ]
