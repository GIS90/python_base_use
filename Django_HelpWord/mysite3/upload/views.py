# -*- coding: utf-8 -*-


from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponse

from .models import UploadFileInfo
from .forms import UploadFileInfoForm

import os


def upload(request):
    """
    upload file to server stored
    :param request:
    :return: Ture or False
    """
    if request.method == 'POST':
        ufi_form = UploadFileInfoForm(request.POST, request.FILES)
        uploadfile = request.FILES.get('file', None)

        if not uploadfile:
            return HttpResponse('no file is upload')

        uploadfile_name, uploadfile_type = os.path.splitext(uploadfile.name)
        uploadfile_path = os.path.abspath(os.path.dirname(__file__))
        uploadfile_path = os.path.join(uploadfile_path, 'files', uploadfile_type)
        if not os.path.exists(uploadfile_path):
            os.makedirs(uploadfile_path)

        with open(os.path.join(uploadfile_path, uploadfile.name), 'wb') as target_file:
            for chunk in uploadfile.chunks():
                target_file.write(chunk)
        if ufi_form.is_valid():
            ufi = UploadFileInfo()
            ufi.user = ufi_form.cleaned_data['user']
            ufi.ip = request.get_host()
            ufi.type = uploadfile_type
            ufi.path = uploadfile_path
            ufi.save()

        return HttpResponse('<h1>%s upload is success</h1>' % uploadfile.name)
    else:
        ufi_form = UploadFileInfoForm()
    return render_to_response('upload.html', {'ufi_form': ufi_form})




