# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=32,default='Title')
    content = models.TextField(null=True)
    #添加创建日期,默认为当前时间auto_now,我们需要修改设为null=True
    pub_time = models.DateTimeField(null=True)


    def __unicode__(self):
        return self.title


