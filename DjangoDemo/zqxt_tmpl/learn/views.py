# coding: utf-8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    string = 'my frist django page'
    tutorlist = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': '自强学堂', 'content': '各种IT技术教程'}
    List = map(str, range(1, 101))
    return render(request, 'index.html', {'List': List})



