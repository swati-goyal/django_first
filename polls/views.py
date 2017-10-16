from django.shortcuts import render
from django.http import HttpResponse, Http404
import random
import time
from .models import Question, Choice
from django.template import loader


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def about(request):
    return HttpResponse("Hello, world. You're at the polls about page.")


def random_page(request):
    t = random.randint(1, 89)
    t1 = time.ctime()
    return HttpResponse("Today's random number is {} and current time is : {} IST".format(t, t1))


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
