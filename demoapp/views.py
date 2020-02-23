from django.views.generic import ListView, DetailView

from . import models


class PostListView(ListView):
    model = models.Post
    title = "Home"


class PostDetailView(DetailView):
    model = models.Post

    def title(self):
        return self.object
