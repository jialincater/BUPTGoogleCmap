# -*- coding: utf-8 -*-
from django import forms
from .models import Camper

class regForm(forms.ModelForm):
    class Meta:
        fields = '__all__'
        model = Camper

class NregForm(forms.Form):
	YEAR_IN_SCHOOL_CHOICES = (
    ('1', '大一'),
    ('2', '大二'),
    ('3', '大三'),
    ('4', '大四'),
    ('5', '研究生'),
)
	mediaC = [("Pr", "Pr"),("Ps", "Ps"),("Ae", "Ae"),("Au", "Au"),("Final Cut Pro", "Final Cut Pro")]
	userC = (("Java", "Java"),("PHP", "PHP"),("HTML/CSS", "HTML/CSS"),("Python", "Python"),("Ruby", "Ruby"),("C/C++", "C/C++"),("Javascript", "Javascript"),("Ruby", "Ruby"))
	name = forms.CharField(label='姓名',max_length=100)
	student_id = forms.IntegerField(label='学号')
	phone = forms.IntegerField(label='手机')
	mail = forms.EmailField(label='邮箱')
	grade = forms.ChoiceField(label='年级',choices=YEAR_IN_SCHOOL_CHOICES,)
	# JAVA = forms.BooleanField(label='JAVA')
	# Python = forms.BooleanField()
	# PHP = forms.BooleanField()
	# JS = forms.BooleanField()
	users = forms.MultipleChoiceField(choices=userC,required=False,widget=forms.CheckboxSelectMultiple,label="勾选你熟练掌握的语言：")
	mediaa = forms.MultipleChoiceField(choices=mediaC,required=False,widget=forms.CheckboxSelectMultiple,label="勾选你熟练掌握的媒体编辑器：")

class modForm(forms.Form):
	SCHOOL_CHOICES = (
    ('信息与通信工程学院', '信息与通信工程学院'),
    ('电子工程学院', '电子工程学院'),
    ('计算机学院', '计算机学院'),
    ('自动化学院', '自动化学院'),
    ('数字媒体与设计艺术学院', '数字媒体与设计艺术学院'),
    ('理学院','理学院'),
    ('公共管理学院', '公共管理学院'),
    ('人文学院', '人文学院'),
    ('国际学院', '国际学院'),
    ('网络教育学院', '网络教育学院'),
    ('继续教育学院', '继续教育学院'),
    ('民族教育学院', '民族教育学院'),
    ('网络技术研究院', '网络技术研究院'),
    ('信息光子学与光通信研究院','信息光子学与光通信研究院'),
    ('马克思主义学院','马克思主义学院'),
)
	

	GENDER_CHOICES = (('男','男'),('女','女'))
	phone = forms.IntegerField(label='手机')
	school = forms.ChoiceField(label='学院',choices=SCHOOL_CHOICES,)
	gender = forms.ChoiceField(label='性别',choices=GENDER_CHOICES,)
	classNo = forms.IntegerField(label='班级，如：2012211122')
