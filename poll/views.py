from django.shortcuts import render
from django.http import HttpResponse, Http404

# Create your views here.
from django.template import loader

from poll.models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('poll/index.html')
    context = {
        'latest_question_list': latest_question_list
    }
    # formatted_date = ([print(q.question_text) for q in latest_questions])
    return render(request, 'poll/index.html', context)


def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question doesn't exist")
    return render(request, 'poll/detail.html', {'question': question})


def result(request, question_id):
    response = "You are looking at the results of question %s"
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You are voting at %s" % question_id)
