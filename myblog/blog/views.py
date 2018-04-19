# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

from . import models

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





