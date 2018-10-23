from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.

from .models import File
from .forms import FileForm

import os


def upload(request):
    if request.method == "POST":
        uf = FileForm(request.POST, request.FILES)
        uf_file = request.FILES.get('file', None)

        if not uf_file:
            return HttpResponse('no file for upload')
        destination = open(uf_file.name, 'wb+')
        for chunk in uf_file.chunks():
            destination.write(chunk)
        destination.close()

        if uf.is_valid():
            user = uf.cleaned_data['user']
            ip = request.get_host()
            path = uf.cleaned_data['file']

            f = File()
            f.user = user
            f.ip = ip
            f.path = path
            f.save()

        return HttpResponse('upload ok!')
    else:
        uf = FileForm()
    return render_to_response('upload.html', {'uf': uf})
