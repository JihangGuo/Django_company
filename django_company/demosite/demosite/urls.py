# -*- coding: UTF-8 -*-

"""demosite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import view

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    url(r'^$',view.index_view),   
    url(r'^admin/', admin.site.urls),
    url('^index/$',view.index_view),
    url('^index/news/(\d+)/$', view.text_view),
    url('^index/projects/(\d+)/$', view.text1_view),
    url('^index/details/(\d+)/$', view.text2_view),
    url('^index/glorys/(\d+)/$', view.text3_view),

    url('^contact/$',view.contact_view),

    url('^about/$',view.about_view,{'template_name':'about.html'}),
    url('^about_1/$', view.about_view, {'template_name': 'about_1.html'}),
    url('^about_2/$', view.about_view, {'template_name': 'about_2.html'}),
    url('^about_3/$', view.about_view, {'template_name': 'about_3.html'}),
    url('^about_4/$', view.about_view, {'template_name': 'about_4.html'}),

    url('^news/$', view.news_view,{'template_name': 'news.html'}),
    url('^news_1/$', view.news_view, {'template_name': 'news_1.html'}),
    url('^news.*/(\d+)/$',view.text_view),

    url('^groupindustry/$', view.group_view, {'template_name': 'groupindustry.html'}),

    url('^jobs/$', view.jobs_view, {'template_name': 'jobs.html'}),
    url('^jobs_1/$', view.jobs_view, {'template_name': 'jobs_1.html'}),
    url('^jobs_2/$', view.jobs_view, {'template_name': 'jobs_2.html'}),
    url('^jobs.*/(\d+)/$', view.text1_view),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

