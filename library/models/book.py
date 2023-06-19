from django.db import models
from django.urls import reverse
from .author import Author


class Book(models.Model):
    name = models.CharField(max_length=60)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, blank=True, null=True)
    genre = models.CharField(max_length=100)
    release_date = models.IntegerField(default=0)
    number_pages = models.IntegerField(default=0)
    summary = models.TextField(default=0, max_length=800)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("book-detail", args=[str(self.pk)])