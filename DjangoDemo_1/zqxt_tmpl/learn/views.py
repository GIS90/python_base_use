# coding: utf-8

from django.shortcuts import render


# Create your views here.


def home(request):
    string = 'hello world'
    tutorialist = ["HTML", "CSS", "jQuery", "Python", "Django"]
    info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    lt = map(str, range(100))
    var = 80
    # return render(request, 'home.html', {'lt': lt, 'tutorialist': tutorialist})
    return render(request, 'home.html')



