# -*- coding: utf-8 -*-


from django import forms


class UploadFileInfoForm(forms.Form):
    user = forms.CharField(max_length=40)
    file = forms.FileField()
