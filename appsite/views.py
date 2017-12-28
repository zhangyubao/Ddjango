# -*- coding:utf-8 -*-
from django.http import HttpResponse


def first_page(request):
    return HttpResponse('<p>你好Python~~~~~~~~~~</p>')


def page(request,mum = 1):
    '''
    此处匹配的url正则表达式
    url(r'^blog/$', views.page)
    url(r'^blog/page(?P<num>[0-9]+)/$', views.page)
    两个url指向了同一个试图
    匹配到第一个的时候默认值是1
    匹配到第二个的时候会被匹配到的值替代----默认值的用法
    '''
