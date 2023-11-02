"""
Vista para administras las otras vistas
"""
from django.shortcuts import render

# Create your views here.
from ..models.book import Book
from ..models.users import User
from ..models.author import Author


def index(request):
    """Function to home site"""
    books = Book.objects.all()
    users = User.objects.all()
    authors = Author.objects.all()

    return render(
        request,
        'library/index.html',
        context={
            "books": books,
            "authors": authors,
            "users": users

        }
    )
