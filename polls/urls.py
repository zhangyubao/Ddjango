from django.conf.urls import url
from . import views


urlpatterns = [

    # ?P<question> 这个表达式用来定义一个名字
    url(r'^$', views.index, name='index'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote$', views.vote, name='vote'),
]
