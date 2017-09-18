# -*- coding: UTF-8 -*-


from django.shortcuts import render_to_response
from edit.models import Details,News,Projects,Glorys,text_index,video_index,logo_index,pic_index
import edit

get_logoo = logo_index.objects.all()[:1]
for haha in get_logoo:
    get_logo = haha.logo_index

def index_view(request):
    get_hq = text_index.objects.all()
    for get_text in get_hq:
        text_hq = get_text.about_index
        pic_hq = get_text.hq_index
    get_new = News.objects.all()[:6]
    get_detail = Details.objects.all()[:6]
    get_glory = Glorys.objects.all()[:6]
    get_project = Projects.objects.all()[:6]
    get_video = video_index.objects.all()


    get_pic = pic_index.objects.all()[:1]

    return render_to_response('index.html',{'pic_hq':pic_hq,'text_hq':text_hq,'get_new':get_new,'get_detail':get_detail,'get_glory':get_glory,'get_project':get_project,'get_video':get_video,'get_logo':get_logo,'get_pic':get_pic,'get_projectt':get_project})

def contact_view(request):
    return render_to_response('contact.html',{'get_logo':get_logo})

def about_view(request,template_name):
    the_impo = Projects.objects.all()[:1]
    return render_to_response(template_name,{'the_impo':the_impo,'get_logo':get_logo})

def news_view(request,template_name):
    the_impo = Projects.objects.all()[:1]

    if (template_name == 'news.html' ):
        get_hqnews = News.objects.filter( news_type = 0)
        return render_to_response(template_name,{'get_allnew':get_hqnews,'the_impo':the_impo,'get_logo':get_logo})

    else:
        get_hynews = News.objects.filter(news_type = 1)
        return render_to_response(template_name,{'get_allnew':get_hynews,'the_impo':the_impo,'get_logo':get_logo})

def group_view(request,template_name):
    the_impo = Projects.objects.all()[:1]
    return render_to_response(template_name,{'the_impo':the_impo,'get_logo':get_logo})

def jobs_view(request,template_name):
    the_impo = Projects.objects.all()[:1]

    if (template_name == 'jobs.html'):
        get_job = Projects.objects.all()
        return render_to_response(template_name,{'get_allpro':get_job,'the_impo':the_impo,'get_logo':get_logo})
    elif(template_name== 'jobs_1.html'):
        get_job1 = Projects.objects.filter(projects_type = 0)
        return render_to_response(template_name,{'get_pro':get_job1,'the_impo':the_impo,'get_logo':get_logo})
    else:
        get_job2 = Projects.objects.filter(projects_type=1)
        return render_to_response(template_name, {'get_pro': get_job2,'the_impo':the_impo,'get_logo':get_logo})

def group_view(request, template_name):
    the_impo = Projects.objects.all()[:1]
    return render_to_response(template_name,{'the_impo':the_impo,'get_logo':get_logo})

def text_view(request,param1):
    the_impo = Projects.objects.all()[:1]

    the_p = param1
    get_index = News.objects.filter(id = the_p)
    for sad in get_index:
        the_title = sad.news_title
        the_text = sad.news_text
        the_time = sad.news_time
        the_pic = sad.news_url
    return render_to_response('text.html',{'the_impo':the_impo,'the_title':the_title,'the_text':the_text,'the_time':the_time,'the_pic':the_pic,'get_logo':get_logo})

def text1_view(request,param1):
    the_impo = Projects.objects.all()[:1]

    the_p = param1

    get_index = Projects.objects.filter(id = the_p)
    for sad in get_index:
        the_title = sad.projects_title
        the_text = sad.projects_text
        the_time = sad.projects_time

        the_pic = sad.projects_url
        the_pic1 = sad.projects_url1
        the_pic2 = sad.projects_url2
        the_pic3 = sad.projects_url3
        the_pic4 = sad.projects_url4
    return render_to_response('text1.html',{'the_impo':the_impo,'the_title':the_title,'the_text':the_text,'the_time':the_time,'the_pic':the_pic,'the_pic1':the_pic1,'the_pic2':the_pic2,'the_pic3':the_pic3,'the_pic4':the_pic4,'get_logo':get_logo})

def text2_view(request,param1):
    the_impo = Projects.objects.all()[:1]


    the_p = param1
    get_index = Details.objects.filter(id = the_p)
    for sad in get_index:
        the_title = sad.details_title
        the_text = sad.details_text
        the_time = sad.details_time
        the_pic = sad.details_url
    return render_to_response('text.html',{'the_impo':the_impo,'the_title':the_title,'the_text':the_text,'the_time':the_time,'the_pic':the_pic,'get_logo':get_logo})

def text3_view(request,param1):
    the_impo = Projects.objects.all()[:1]


    the_p = param1
    get_index = Glorys.objects.filter(id = the_p)
    for sad in get_index:
        the_title = sad.glorys_title
        the_text = sad.glorys_text
        the_time = sad.glorys_time
        the_pic = sad.glorys_url
    return render_to_response('text.html',{'the_impo':the_impo,'the_title':the_title,'the_text':the_text,'the_time':the_time,'the_pic':the_pic,'get_logo':get_logo})
