# -*- coding: utf-8 -*-


from django import forms


class FileInfoForm(forms.Form):
    user = forms.CharField(max_length=40)
    # ip = forms.CharField(max_length=40)
    uploadfile = forms.FileField()
