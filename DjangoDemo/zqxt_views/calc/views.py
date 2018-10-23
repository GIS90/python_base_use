from django.shortcuts import render

# Create your views here.


from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def add3(request):
    return HttpResponse('add3')


def index(request):
    return render(request, 'home.html')


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )


def old_add3_redirect(request):
    return HttpResponseRedirect(
        reverse('add3')
    )


