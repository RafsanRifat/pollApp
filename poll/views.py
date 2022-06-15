from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
from poll.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)


def result(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting at %s" % question_id)
