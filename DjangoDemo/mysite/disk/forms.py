# -*- coding: utf-8 -*-

from django import forms
"""
------------------------------------------------
describe: 
------------------------------------------------
"""


class UserForm(forms.Form):
    username = forms.CharField()
    headimg = forms.FileField()






