# coding: utf-8
from django.shortcuts import render
from django.shortcuts import render_to_response

from django.http import HttpResponse

from .forms import FileInfoForm
from .models import FileInfo



def upload_file(request):
    if request.method is 'POST':
        uf_form = FileInfoForm(request.POST, request.FILES)
        # uf_file = request.FILES.get('uploadfile', None)

        # if not uf_file:
        #     return HttpResponse('no file for upload')
        # destination = open(os.path.join("E:\\upload", uf_file.name), 'wb+')
        # for chunk in myFile.chunks():
        #     destination.write(chunk)
        # destination.close()

        if uf_form.is_valid():
            user = uf_form.cleaned_data['user']
            ip = request.get_host()
            path = uf_form.cleaned_data['uploadfile']

            uploadfile = FileInfo()
            uploadfile.user = user
            uploadfile.ip = ip
            uploadfile.path = path
            uploadfile.save()

            return HttpResponse('ok')
    else:
        uf_form = FileInfoForm()

    return render_to_response('upload.html', {'uf_form': uf_form})


