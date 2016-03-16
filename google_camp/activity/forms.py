# -*- coding: utf-8 -*-
from django import forms
from camper_mng.models import Camper

class NregForm(forms.Form):
	name = forms.CharField(label='姓名',max_length=100)
	phone = forms.IntegerField(label='手机')