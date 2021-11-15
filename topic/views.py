from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Topic
from django.views import View
from django.views.generic import ListView, DetailView

# Create your views here.

class TopicListView(ListView):
    model = Topic
    # template_name = 'topic/snippet_list.html'


class TopicDetailView(DetailView):
    model = Topic
    # template_name = 'topic/snippet_detail.html'
