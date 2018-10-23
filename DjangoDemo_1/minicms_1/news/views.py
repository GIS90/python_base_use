# coding: utf-8


from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse('欢迎来到自强学习')


def column_detail(request):
    return HttpResponse('column slug: ' + column_slug)


def article_detail(request, article_slug):
    return HttpResponse('article slug: ' + article_slug)
