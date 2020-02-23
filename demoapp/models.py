from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=300)
    content = models.TextField()
    published_at = models.DateTimeField()

    class Meta:
        ordering = (
            "-published_at",
        )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("demoapp:detail", args=(self.pk,))
