# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=32,default='Title',verbose_name=u'文章标题')
    content = models.TextField(null=True,verbose_name=u'文章内容')
    #添加创建日期,默认为当前时间auto_now,我们需要修改设为null=True
    pub_time = models.DateTimeField(null=True)

    def __unicode__(self):
        return self.title,self.content

class Photo(models.Model):
    photo_title = models.CharField(max_length=32,default='Photo_title',verbose_name=u'图片标题')
    photo_content = models.TextField(null=True,verbose_name=u'图片内容')
    photo_address = models.CharField(max_length=50,verbose_name=u'图片地址')

    def __unicode__(self):
        return self.photo_title,self.photo_content


