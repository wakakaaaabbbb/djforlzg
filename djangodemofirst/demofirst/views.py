from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question
from django.shortcuts import render, get_object_or_404


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('demofirst/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    output = ', '.join([q.question_text for q in latest_question_list])
    # return HttpResponse(template.render(context, request))
    return render(request, 'demofirst/index.html', context)


def hello(request):
    return HttpResponse('hello')


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'demofirst/detail.html', {'question': question})
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404
    # return render(request, 'demofirst/detail.html', {'question': question})


def results(request, question_id):
    return HttpResponse(f"you are looking at the result of question {question_id}")


def vote(request, question_id):
    return HttpResponse(f"you are voting on question {question_id}")



