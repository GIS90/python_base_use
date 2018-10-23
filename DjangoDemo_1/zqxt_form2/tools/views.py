from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from forms import *


def index(request):

    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(a + b))
    else:
        form = AddForm()
    return render(request, 'index.html', {'form': form})

