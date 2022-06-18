from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.
from django.template import loader

from poll.models import Question, Choice


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
        return render(request, 'poll/404.html', {'error': 'There is no question with this id'})
        raise Http404("Question doesn't exist")
    return render(request, 'poll/detail.html', {'question': question})


def result(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'poll/result.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
        print(request.POST)
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form
        return render(request, 'poll/detail.html', {
            'question': question,
            'error_message': "You don't select a choice"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()

        return HttpResponseRedirect(reverse('poll:result', args=(question.id,)))
