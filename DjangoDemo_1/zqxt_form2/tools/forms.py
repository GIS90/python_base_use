# -*- coding: utf-8 -*-
"""
------------------------------------------------
describe: 
------------------------------------------------
"""

from django import forms


__version__ = "v.10"
__author__ = "PyGo"
__time__ = "2017/2/27"


class AddForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()





