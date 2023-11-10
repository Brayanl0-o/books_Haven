"""
Vistas genericas para administrar los autores
"""
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from ..models.author import Author


class AuthorListView(generic.ListView):
    """
    Vista genérica para mostrar una lista de autores.
    """
    model = Author
    context_object_name = 'author_list'
    template_name = 'library/author/author_list.html'


class AuthorDetailView(generic.DetailView):
    """
    Vista genérica para mostrar los detalles de un Author.
    """
    model = Author
    context_object_name = 'author'
    template_name = 'library/author/author_detail.html'


class AuthorCreateView(generic.CreateView):
    """
    Vista genérica para crear un nuevo Author.
    """
    model = Author
    context_object_name = 'author'
    fields = [
        'name',
        'birth_date',
        'death_date',
        'books'
    ]
    template_name = 'library/author/author_create.html'


class AuthorEditView(UpdateView):
    """
    Vista genérica para editar los detalles de un author existente.
    """
    model = Author
    template_name = 'library/author/author_edit.html'
    fields = ['name', 'birth_date', 'death_date',
              'books']
    success_url = reverse_lazy('authors')


class AuthorDeleteView(DeleteView):
    """
    Vista genérica para eliminar un author existente.
    """
    model = Author
    template_name = 'library/author/author_delete.html'
    fields = ['name', 'birth_date', 'death_date',
              'books']
    success_url = reverse_lazy('authors')
