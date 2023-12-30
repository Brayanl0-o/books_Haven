"""
Vistas genericas para administrar los libros
"""
from django.urls import reverse
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from ..models.book import Book
from ..models.author import Author
from .forms import BookForm
# from .forms import BookForm
# from django.views.generic.edit import CreateView

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
    form_class = BookForm
    template_name = 'library/book/book_create.html'

    def form_valid(self, form):
        # Sobrescribe el método form_valid para personalizar el comportamiento
        response = super().form_valid(form)

        # Asocia el libro con el autor
        author_id = self.request.POST.get('author')
        if author_id:
            author = get_object_or_404(Author, pk=author_id)
            author.books.add(self.object)

        return response
 
class BookEditView(UpdateView):
    """
    Vista genérica para editar los detalles de un libro existente.
    """
    model = Book
    template_name = 'library/book/book_edit.html'
    fields = ['name', 'author','cover_page' , 'link_dowload_free','link_dowload_buy', 'genre', 'release_date', 'number_pages', 'summary']

    def form_valid(self, form):
        # Obtiene el autor original antes de la edición
        old_author = Book.objects.get(pk=self.object.pk).author

        # Desvincula el libro del autor anterior antes de asociarlo al nuevo autor
        if old_author:
            old_author.books.remove(self.object)
            print(f"Libro desvinculado del autor anterior: {self.object} del autor: {old_author.name}")

        # Asocia el libro con el nuevo autor
        response = super().form_valid(form)
        author_id = self.request.POST.get('author')
        if author_id:
            new_author = get_object_or_404(Author, pk=author_id)
            new_author.books.add(self.object)
            print(f"Libro asociado al nuevo autor: {self.object} al autor: {new_author.name}")

        return response
    def get_success_url(self):
        book_pk = self.object.pk
        return reverse('book-detail', kwargs={'pk': book_pk})


class BookDeleteView(DeleteView):
    """
    Vista genérica para eliminar un libro existente.
    """
    model = Book
    template_name = 'library/book/book_delete.html'
    fields = ['fname', 'lname', 'document_type',
              'document_number', 'age']
    success_url = reverse_lazy('books')
