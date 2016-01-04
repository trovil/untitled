"""untitled URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from mysite.views import hello,current_datetime,hours_ahead,search,contact
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^hello/$', hello),
    url(r'^time/$', current_datetime),
    url(r'^time/plus/(\d{1,2})/$', hours_ahead),
    url(r'^search/$', search),
    url(r'^contact/$', contact),
    url(r'^registration/$', 'regisry.reg.register'),
    url(r'^login/$', 'regisry.reg.login'),
    url(r'^logout/$', 'regisry.reg.logout'),
    url(r'^$', 'blog.views.post_list', name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', 'blog.views.post_detail', name='post_detail'),
    url(r'^post/new/$', 'blog.views.post_new', name='post_new'),
    url(r'^post/(?P<pk>[0-9]+)/edit/$', 'blog.views.post_edit', name='post_edit'),
    url(r'^drafts/$', 'blog.views.post_draft_list', name='post_draft_list'),
    url(r'^post/(?P<pk>[0-9]+)/publish/$', 'blog.views.post_publish', name='post_publish'),
    url(r'^post/(?P<pk>[0-9]+)/remove/$', 'blog.views.post_remove', name='post_remove'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^post/(?P<pk>[0-9]+)/comment/$', 'blog.views.add_comment_to_post', name='add_comment_to_post'),
    url(r'^comment/(?P<pk>[0-9]+)/approve/$', 'blog.views.comment_approve', name='comment_approve'),
    url(r'^comment/(?P<pk>[0-9]+)/remove/$', 'blog.views.comment_remove', name='comment_remove'),
]
