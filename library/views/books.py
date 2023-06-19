from django.views import generic
from ..models.book import Book
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView


class bookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'library/book/book_list.html'


class bookDetailView(generic.DetailView):
    model = Book
    context_object_name = 'book'
    template_name = 'library/book/book_detail.html'


class bookCreateView(generic.CreateView):
    model = Book
    context_object_name = 'book'
    fields = [
        'name',
        'author',
        'genre',
        'release_date',
        'number_pages',
        'summary'
    ]
    template_name = 'library/book/book_form.html'


class bookEditView(UpdateView):
    model = Book
    template_name = 'library/book/book_edit.html'
    fields = ['name', 'author', 'genre',
              'release_date', 'number_pages', 'summary']
    success_url = reverse_lazy('books')

class bookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book/book_delete.html'
    fields = ['fname', 'lname', 'document_type',
              'document_number', 'age']
    success_url = reverse_lazy('books')