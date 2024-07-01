from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question

# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(request, "polls/index.html", {"latest_question_list": latest_question_list})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})

def results(request, question_id):
    return HttpResponse("You're looking at the results of question %s" % question_id)


def vote(request, question_id):
    return HttpResponse(f"You're voting on quesiton {question_id}")

