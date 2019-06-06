"""myjkbbs URL Configuration

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
from django.contrib import admin
from home import views as home_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',home_view.test1),
    url(r'^register$',home_view.register),
    url(r'^login$',home_view.login),
    url(r'^posts$',home_view.postlist),
    url(r'^sections$',home_view.sectionlist),
    url(r'^sectionpostlist/(.*?)$',home_view.sectionpostlist),
    url(r'^postdetail/(.*?)$',home_view.postdetail),
    url(r'^postsub$',home_view.postsub),
    url(r'^comment/(.*?)$',home_view.comment),
    url(r'^logout$',home_view.logout),
    url(r'^cmodify/(.*?)/$',home_view.cmodify),
    url(r'^chat/(.*?)/$',home_view.chat),
]
