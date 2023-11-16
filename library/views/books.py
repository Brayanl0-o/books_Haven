"""
Vistas genericas para administrar los libros
"""
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from ..models.book import Book


class BookListView(generic.ListView):
    """
    Vista genérica para mostrar una lista de libros.
    """
    model = Book
    context_object_name = 'book_list'
    template_name = 'library/book/book_list.html'


class BookDetailView(generic.DetailView):
    """
    Vista genérica para mostrar los detalles de un libro.
    """
    model = Book
    context_object_name = 'book'
    template_name = 'library/book/book_detail.html'


class BookCreateView(generic.CreateView):
    """
    Vista genérica para crear un nuevo libro.
    """
    model = Book
    context_object_name = 'book'
    fields = [
        'name',
        'author',
        'cover_page' ,
        'genre',
        'release_date',
        'number_pages',
        'summary'
    ]
    template_name = 'library/book/book_create.html'


class BookEditView(UpdateView):
    """
    Vista genérica para editar los detalles de un libro existente.
    """
    model = Book
    template_name = 'library/book/book_edit.html'
    fields = ['name', 'author','cover_page' , 'genre',
              'release_date', 'number_pages', 'summary']
    success_url = reverse_lazy('books')


class BookDeleteView(DeleteView):
    """
    Vista genérica para eliminar un libro existente.
    """
    model = Book
    template_name = 'library/book/book_delete.html'
    fields = ['fname', 'lname', 'document_type',
              'document_number', 'age']
    success_url = reverse_lazy('books')
