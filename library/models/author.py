"""
Módulo que contiene la definición del modelo Author.

Este módulo define el modelo Author que representa a los autores de libros.
"""
from django.db import models
from django.urls import reverse

class Author(models.Model):
    """
    Modelo que representa a un autor de libros.

    Atributos:
    name (str): El nombre del autor.
    birth_date (date): La fecha de nacimiento del autor.
    death_date (date): La fecha de fallecimiento del autor.
    books (ManyToManyField): Los libros escritos por este autor.
    """

    name = models.CharField(max_length=100)
    birth_date = models.DateField(null=True, blank=True)
    death_date = models.DateField(null=True, blank=True)
    biography = models.TextField(blank=True,default=' ', max_length=800)
    photo_author = models.CharField(
        max_length=250,
        default='https://img.uefa.com/imgml/TP/players/39/2023/324x324/250058368.jpg'
        )
    books = models.ManyToManyField('Book', related_name='authors', blank=True)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """
        Devuelve una representación en cadena del autor.

        Returns:
        str: El nombre del autor.
        """
        return reverse("author-detail", args=[str(self.pk)])
