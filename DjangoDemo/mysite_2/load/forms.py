# -*- coding: utf-8 -*-
from django import forms

"""
------------------------------------------------
describe: 
------------------------------------------------
"""


class UserForm(forms.Form):
    username = forms.CharField()
    loadfile = forms.FileField()
