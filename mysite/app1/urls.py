from django.urls import path
from django.conf.urls import include, url
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('articles', views.articles , name = 'articles'),
    path('news', views.news, name = 'news'),
    path('createart',views.createarticles),
    path('sourcepage', views.sourcepage),
    path('handlecreatearticles',views.handlecreatearticles, name='handlecreatearticles')
    ]
