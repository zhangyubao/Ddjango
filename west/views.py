# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def app_site(request):
    return HttpResponse('<p>其他APP Site' + str(request) + '</p>')


def templay(request):
    context = {}
    context['label'] = 'Hello World'
    return render(request, 'templay.html', context)

