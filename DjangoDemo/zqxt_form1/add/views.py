from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return render(request, 'index.html')


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    sum = int(a) + int(b)

    return render(request, 'add.html', {'sum': sum})