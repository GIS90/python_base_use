# coding:utf-8


from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
# Create your views here.


def add(request):
    x = request.GET['x']
    y = request.GET['y']

    sum = int(x) + int(y)
    return HttpResponse(str(sum))


def add2(request, a, b):
    if not isinstance(a, int):
        a = int(a)
    if not isinstance(b, int):
        b = int(b)

    c = a + b
    return HttpResponse(c)


def index(request):
    return render(request, 'home.html')
