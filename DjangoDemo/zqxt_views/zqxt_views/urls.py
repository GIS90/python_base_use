"""zqxt_views URL Configuration

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
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from calc import views as calc_views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^add/$', calc_views.add, name='add'),
    url(r'^add2/(\d+)/(\d+)/$', calc_views.add2, name='add2'),
    url(r'^add3/$', calc_views.add3, name='add3'),
    url(r'^index/$', calc_views.index, name='home'),
    url(r'^new_add2/(\d+)/(\d+)/$', calc_views.old_add2_redirect),
    url(r'^new_add3/$', calc_views.old_add3_redirect),
]
