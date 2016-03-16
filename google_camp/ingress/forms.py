# -*- coding: utf-8 -*-
from django import forms
class logForm(forms.Form):
	name = forms.CharField(max_length=10)
	password = forms.CharField(max_length=100)

class ingressForm(forms.Form):
	YEAR_IN_SCHOOL_CHOICES = (
    ('1', 1),
    ('2', 2),
    ('3', 3),
    ('4', 4),
    ('5', 5),
    ('6', 6),
    ('7', 7),
    ('8', 8),
    ('9', 9),
    ('10', 10),
    ('11', 11),
    ('12', 12),
    ('13', 13),
    ('14', 14),
	('15', 15),
	('16', 16),
)
	name = forms.CharField(label='特工ID',max_length=10,required=True)
	phone = forms.IntegerField(label='手机',required=False)
	mail = forms.EmailField(label='邮箱',required=True,)
	level = forms.ChoiceField(label='等级',choices=YEAR_IN_SCHOOL_CHOICES,required=True,initial=8)
	password = forms.CharField(label='密码(尽量设简单，没啥重要信息)', max_length=100, widget = forms.PasswordInput)
	password2 = forms.CharField(label='再输一遍（密码用于注册成功以后在右上角登录哦~）', max_length=100,widget = forms.PasswordInput())
	eat = forms.BooleanField(required=False,label='要一起吃吃吃')