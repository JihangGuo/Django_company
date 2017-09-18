# -*- coding: UTF-8 -*-
from django.db import models



class News(models.Model):
    news_title = models.CharField(max_length=50,verbose_name=u"新闻标题")
    news_url = models.FileField(upload_to='news_pic/',blank=False,default="",verbose_name=u"新闻图片")
    news_text = models.TextField(default="",verbose_name=u"新闻正文")
    news_time = models.DateField(auto_now=True,verbose_name=u"新闻时间")
    get_newtype = (
        (0,u'海桥快讯'),
        (1,u'行业动态'),
    )
    news_type = models.IntegerField(choices=get_newtype)
    def __unicode__(self):
        return self.news_title

class Details(models.Model):
    details_title = models.CharField(max_length=50,verbose_name=u"行业动态标题")
    details_url = models.FileField(upload_to='details_pic/',blank=False,default="",verbose_name=u"行业动态图片")
    details_text = models.TextField(default="",verbose_name=u"行业动态正文")
    details_time = models.DateField(auto_now=True,verbose_name=u"行业动态时间")
    def __unicode__(self):
        return self.details_title

class Projects(models.Model):
    projects_title = models.CharField(max_length=50,verbose_name=u"项目名称")

    projects_url = models.FileField(upload_to='projects_pic/',blank=False,default="",verbose_name=u"项目大图")
    projects_url1 = models.FileField(upload_to='projects_pic/',blank=False,default="",verbose_name=u"细节小图1")
    projects_url2 = models.FileField(upload_to='projects_pic/',blank=False,default="",verbose_name=u"细节小图2")
    projects_url3 = models.FileField(upload_to='projects_pic/',blank=False,default="",verbose_name=u"细节小图3")
    projects_url4 = models.FileField(upload_to='projects_pic/',blank=False,default="",verbose_name=u"细节小图4")

    projects_text = models.TextField(default="",verbose_name=u"项目说明")
    projects_time = models.DateField(auto_now=True,verbose_name=u"项目时间")
    get_protype = (
        (0, u'公寓住所/酒店'),
        (1, u'商业工程'),
    )
    projects_type = models.IntegerField(choices=get_protype,verbose_name=u"项目类型")
    def __unicode__(self):
        return self.projects_title

class Glorys(models.Model):
    glorys_title = models.CharField(max_length=50,verbose_name=u"奖项名称")
    glorys_url = models.FileField(upload_to='glorys_pic/',blank=False,default="",verbose_name=u"奖项图片")
    glorys_text = models.TextField(default="",verbose_name=u"奖项正文")
    glorys_time = models.DateField(auto_now=True,verbose_name=u"获奖时间")
    def __unicode__(self):
        return self.glorys_title

class pic_index(models.Model):
    pic_index = models.FileField(upload_to='index_pic/',blank=False,default="",verbose_name=u"首页大图")
    def __unicode__(self):
        return u"首页图片"

class logo_index(models.Model):
    logo_index = models.FileField(upload_to='index_logo/',blank=False,default="",verbose_name=u"公司logo图")
    def __unicode__(self):
        return u"logo图"

class text_index(models.Model):
    about_index = models.TextField(default="",verbose_name=u"首页公司简介")
    hq_index = models.FileField(upload_to='index_text/',blank=False,default="",verbose_name=u"公司图片（小）")
    def __unicode__(self):
        return u"首页公司介绍"

class video_index(models.Model):
    video_index = models.FileField(upload_to='index_video/',blank=False,default="",verbose_name=u"首页宣传视频")
    def __unicode__(self):
        return u"公司介绍视频"

