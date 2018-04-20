from django.conf.urls import url,include

from . import views

urlpatterns = [
    url(r'^index/$', views.index),
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page,name='article_page'),
    url(r'^edit/(?P<article_id>[0-9]+)$', views.edit_page,name='edit_page'),
    url(r'^edit/action$', views.edit_action,name='edit_action'),
    url(r'^photo/$', views.photo_page),
    url(r'^photo/(?P<photo_id>[0-9]+)/$', views.photo_page, name='photo_page'),
    url(r'^editp/(?P<photo_id>[0-9]+)$', views.edit_photo, name='edit_photo'),
    url(r'^editp/photo_action$', views.edit_photo_action, name='edit_photo_action'),
]





