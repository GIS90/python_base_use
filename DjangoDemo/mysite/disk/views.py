from django.shortcuts import render
from django.shortcuts import render_to_response
# Create your views here.

from django.http import HttpResponse

from .forms import UserForm
from .models import User


def register(request):
    if request.method is 'POST':
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            username = uf.cleaned_data['username']
            headimg = uf.cleaned_data['headimg']
            user = User()
            user.username = username
            user.headimg = headimg
            user.save()
            return HttpResponse('upload ok')
    else:
        uf = UserForm()
    return render_to_response('register.html', {'uf': uf})
