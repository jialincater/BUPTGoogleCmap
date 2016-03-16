# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse
import requests
# Create your views here.
def news(request):
    return render(request,'news.html')
