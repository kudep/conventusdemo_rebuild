"""main URL Configuration

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
from . import views


urlpatterns = [
    url(r'^/$', views.story_dev, name='story_dev'),
    url(r'^/(?P<story_id>\d{0,50})/$', views.editing_story, name='editing_story'),
    url(r'^/new_story/', views.new_story, name='new_story'),
    url(r'^/(?P<story_id>\d{0,50})/(?P<scene_id>\d{0,50})/$', views.editing_scene, name='editing_scene'),
    url(r'^/(?P<story_id>\d{0,50})/new_scene/$', views.new_scene, name='new_scene'),
    url(r'^/(?P<story_id>\d{0,50})/(?P<scene_id>\d{0,50})/(?P<answer_id>\d{0,50})/$', views.editing_answer, name='editing_answer'),
    url(r'^/(?P<story_id>\d{0,50})/(?P<scene_id>\d{0,50})/new_answer/$', views.new_answer, name='new_answer'),
    url(r'^/(?P<story_id>\d{0,50})/(?P<scene_id>\d{0,50})/(?P<answer_id>\d{0,50})/(?P<psy_char_id>\d{0,50})/$', views.editing_psy_char, name='editing_psy_char'),
]
