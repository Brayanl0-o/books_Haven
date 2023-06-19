from django.shortcuts import render

# Create your views here.
from ..models.book import Book
from ..models.users import User
from ..models.author import Author



def index(request):
    """Function to home site"""
    book = Book.objects.all()
    user = User.objects.all()
    author = Author.objects.all()

    return render(
        request,
        'library/index.html',
        context={
            "books": book,
            "authors": author,
            "users": user

        }
    )
