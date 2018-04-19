# -*- coding: utf-8 -*-
from django.shortcuts import render

def index(request):
    return render(request,'blog2/index.html',{'hello':'hello,blog2'})

