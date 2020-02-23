from django.views.generic import ListView, DetailView

from . import models


class PostListView(ListView):
    model = models.Post


class PostDetailView(DetailView):
    model = models.Post
