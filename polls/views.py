from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader
from .models import Question

# Create your views here.


# 第一个视图
def index(request):

    # return HttpResponse('Hello World. You\'re at the polls index.')

    # latest_question_list = Question.objects.order_by('publish_date')[:5]
    # output = '</br>'.join(
    #     p.question_text for p in latest_question_list)
    # return HttpResponse(output)
    latest_question_list = Question.objects.order_by('publish_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context))
    return HttpResponse(template.render(context))


# 问题详情页
def detail(request, question_id):
    return HttpResponse('You are looking at %s' % question_id)


# 投票结果页面
def results(request, question_id):
    response = 'You are looking at the results of question %s'
    return HttpResponse(response % question_id)


# 投票页面
def vote(request, question_id):
    return HttpResponse('You\'re voting on question %s' % question_id)
    pass
