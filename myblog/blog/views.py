# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from . import models

#记录库模块
def index(request):
    articles = models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
#如果id等于0，返回页面，强化转化为字符串
    if str(article_id) == '0':
        return render(request, 'blog/edit_page.html')
#取出article对象
    article = models.Article.objects.get(pk=article_id)
    return render(request,'blog/edit_page.html',{'article':article})

#方法
def edit_action(request):
#取数据 默认值TITLE
    title = request.POST.get('title','TITLE')
    content = request.POST.get('content','CONTENT')
    article_id =request.POST.get('article_id','0')
    if article_id=='0':
        # 创建文章,对象创建
        models.Article.objects.create(title=title, content=content)
        # 提交之后返回到首页
        articles = models.Article.objects.all()
        return render(request,'blog/index.html',{'articles':articles})

    article = models.Article.objects.get(pk=article_id)
    article.title = title
    article.content= content
    article.save()
#返回文章的页面
    return render(request,'blog/article_page.html',{'article':article})

#图片库模块
def Photo(request):
    photos = models.Photo.objects.all()
    return render(request,'blog/index.html',{'photos':photos})

def photo_page(request,photo_id):
    photo = models.Photo.objects.get(pk=photo_id)
    return render(request,'blog/photo_page.html',{'photo':photo})

def edit_photo(request,photo_id):
    if str(photo_id) == '0':
        return render(request, 'blog/edit_photo.html')
    photo = models.Photo.objects.get(pk=photo_id)
    return render(request,'blog/edit_photo.html',{'photo':photo})

def edit_photo_action(request):
    photo_title = request.POST.get('photo_title','PHOTO_TITLE')
    photo_content = request.POST.get('photo_content','PHOTO_CONTENT')
    photo_adress = request.POST.get('photo_adress','PHOTO_ADRESS')
    photo_id =request.POST.get('photo_id','0')
    if photo_id=='0':
        models.Photo.objects.create(photo_title=photo_title, photo_content=photo_content,photo_adress=photo_adress)
        photos = models.Photo.objects.all()
        return render(request,'blog/photo.html',{'photos':photos})
    photo = models.Article.objects.get(pk=photo_id)
    photo.photo_title = photo_title
    photo.photo_content= photo_content
    photo.photo_address= photo_adress
    photo.save()
    return render(request,'blog/photo_page.html',{'photo':photo})


