from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.shortcuts import render
from .forms import UserForm
from .models import User


def load(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, request.FILES)

        if uf.is_valid():
            username = uf.cleaned_data['username']
            loadfile = uf.cleaned_data['loadfile']
            user = User()
            user.username = username
            user.loadfile = loadfile
            user.save()
            return HttpResponse('upload ok')
    else:
        uf = UserForm()
    return render_to_response('register.html', {'uf': uf})
