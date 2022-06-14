from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, This is the first view")

def detail(request, question_id):
    return HttpResponse("You are looking at question %s" % question_id)
