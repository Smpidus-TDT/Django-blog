# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Article
from models import Photo

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','content','pub_time')
    list_filter = ('pub_time',)

admin.site.register(Article,ArticleAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('photo_title','photo_content','photo_address')


admin.site.register(Photo,PhotoAdmin)
