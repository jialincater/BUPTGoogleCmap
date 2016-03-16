# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.
class Camper(models.Model):
    name = models.CharField(max_length=10)
    student_id = models.IntegerField()
    phone = models.IntegerField(primary_key=True)
    classNo = models.IntegerField(default=2012211122)
    gender = models.CharField(max_length=2,default="男")
    school = models.CharField(max_length=20,default="信息与通信工程学院")
    mail = models.EmailField(default="hi@hi.hi")
    grade = models.CharField(max_length=10)
    canJAVA = models.BooleanField(default=False)
    canPHP = models.BooleanField(default=False)
    canC = models.BooleanField(default=False)
    canPython = models.BooleanField(default=False)
    canJS = models.BooleanField(default=False)
    canHTML = models.BooleanField(default=False)
    canRuby = models.BooleanField(default=False)
    canPr = models.BooleanField(default=False)
    canPs = models.BooleanField(default=False)
    canAe = models.BooleanField(default=False)
    canAu = models.BooleanField(default=False)
    canFCP = models.BooleanField(default=False)
    GDG = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name