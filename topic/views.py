from django.http import HttpResponse, Http404
from django.template import loader
from django.shortcuts import get_object_or_404, render

from .models import Topic

# Create your views here.
def index(request):
    return HttpResponse("Hello World from Topics")

def detail(request, topic_id):

    topic = get_object_or_404(Topic, pk=topic_id)

    context = {"topic": topic}

    return render(request, "topic/detail.html", context)
