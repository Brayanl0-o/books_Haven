from django.views import generic
from ..models.author import Author
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView


class authorListView(generic.ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'library/author/author_list.html'


class authorDetailView(generic.DetailView):
    model = Author
    context_object_name = 'author'
    template_name = 'library/author/author_detail.html'


class authorCreateView(generic.CreateView):
    model = Author
    context_object_name = 'author'
    fields = [
       'name', 
       'birth_date', 
       'death_date',
        'books'
    ]
    template_name = 'library/author/author_form.html'
   

class authorEditView(UpdateView):
    model = Author
    template_name = 'library/author/author_edit.html'
    fields = ['name', 'birth_date', 'death_date',
              'books']
    success_url = reverse_lazy('authors')

class authorDeleteView(DeleteView):
    model = Author
    template_name = 'library/author/author_delete.html'
    fields = ['name', 'birth_date', 'death_date',
              'books']
    success_url = reverse_lazy('authors')
