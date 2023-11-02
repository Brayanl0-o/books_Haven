"""
Módulo que contiene la definición del modelo users

Este módulo define el modelo Author que representa los usuarios.
"""
from django.db import models
from django.urls import reverse


class User(models.Model):
    """
    Modelo que representa a un usuario.

    Atributos:
    first_name (str): El nombre del usuario.
    last_name (str): El apellido del usuario (opcional).
    document_type (str): Tipo de documento del usuario.
    document_number (int): Número de documento del usuario.
    age (int): Edad del usuario.
    """
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    DOCUMENT_TYPE_CHOICE = (
        ("CC", "Cedula de Ciudadania"),
        ("PPT", "Permiso de Protección Temporal"),
        ("CE", "Cedula de Extranjeria"),
        ("TI", "Tarjeta de Identidad"),
        ("CL", "Code Librery")
    )
    document_type = models.CharField(
        max_length=3, choices=DOCUMENT_TYPE_CHOICE, default="CC")
    document_number = models.IntegerField(default=0)
    age = models.IntegerField(default=0)

    def __str__(self):
        return "Bienvenid@ " + self.first_name + " " + self.last_name + " a La libreria de Cuyeca."

    def get_absolute_url(self):
        """
        Devuelve la URL absoluta para ver los detalles del usuario.
        """
        return reverse("users-detail", args=[str(self.pk)])
