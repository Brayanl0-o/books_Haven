from django.db import models
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    birth_date = models.DateField()
    death_date = models.DateField()
    books = models.ManyToManyField('Book', related_name='authors', blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("author-detail", args=[str(self.pk)])

    
