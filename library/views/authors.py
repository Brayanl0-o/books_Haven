"""
Vistas genericas para administrar los autores
"""
from django.views import generic
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import UpdateView, DeleteView
from ..models.author import Author
from .forms import AuthorForm

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
    fields = ['name', 'birth_date', 'death_date', 'biography', 'photo_author']
    # fields = [
    #     'name',
    #     'birth_date',
    #     'death_date',
    #     'biography',
    #     'photo_author',
    #     'books'
    # ]
    
    template_name = 'library/author/author_create.html'
    def form_valid(self, form):
        # Sobrescribe el método form_valid para personalizar el comportamiento
        response = super().form_valid(form)

        # Asocia el libro con el autor
        author_id = self.request.POST.get('author')
        if author_id:
            author = get_object_or_404(Author, pk=author_id)
            author.books.add(self.object)

        return response

class AuthorEditView(UpdateView):
    """
    Vista genérica para editar los detalles de un author existente.
    """
    model = Author
    template_name = 'library/author/author_edit.html'
    fields = ['name', 'birth_date', 'death_date', 'biography', 'photo_author']
    
    def get_success_url(self):
        author_pk = self.object.pk
        return reverse('author-detail', kwargs={'pk': author_pk})


class AuthorDeleteView(DeleteView):
    """
    Vista genérica para eliminar un author existente.
    """
    model = Author
    template_name = 'library/author/author_delete.html'
    fields = ['name', 'birth_date', 'death_date', 
              'books']
    success_url = reverse_lazy('authors')
