"""
Módulo que contiene la definición del modelo books

Este módulo define el modelo Author que representa los libros.
"""
from django.db import models
from django.urls import reverse
from .author import Author


class Book(models.Model):
    """
    Modelo que representa un libro.

    Atributos:
    name (str): El nombre del libro.
    author (Author): El autor del libro.
    genre (str): El género del libro.
    release_date (int): El año de publicación del libro.
    number_pages (int): El número de páginas del libro.
    summary (str): Un resumen del contenido del libro.
    """

    name = models.CharField(max_length=60)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, default='No hay un autor asociado', blank=True, null=True)
    cover_page = models.CharField(
        max_length=200,
        default='https://img.freepik.com/vector-premium/adorno-oro-sobre-fondo-cuero-puede-utilizar-como-tarjeta-invitacion-ilustracion-vectorial_443748-1466.jpg'
        )
    link_dowload_free = models.CharField(
        max_length=250,
        default='No hay enlace'
    )
    link_dowload_buy = models.CharField(
        max_length=250,
        default='No hay enlace'
    )
    genre = models.CharField(max_length=100)
    release_date = models.DateField(default=' ')
    # release_date = models.IntegerField(default=0)
    number_pages = models.IntegerField(default=0)
    summary = models.TextField(default='', max_length=800)

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        """
        Devuelve la URL absoluta para ver los detalles del libro.
        """
        return reverse("book-detail", args=[str(self.pk)])
