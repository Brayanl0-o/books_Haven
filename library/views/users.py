from django.views import generic
from ..models.users import User
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView


class userListView(generic.ListView):
    model = User
    context_object_name = 'user_list'
    template_name = 'library/user/user_list.html'


class userDetailView(generic.DetailView):
    model = User
    context_object_name = 'user'
    template_name = 'library/user/user_detail.html'


class userCreateView(generic.CreateView):
    model = User
    context_object_name = 'user'
    fields = [
        'first_name',
        'last_name',
        'document_type',
        'document_number',
        'age'
    ]
    template_name = 'library/user/user_form.html'
    success_url = reverse_lazy('users')


class userEditView(UpdateView):
    model = User
    template_name = 'library/user/user_edit.html'
    fields = ['first_name', 'last_name', 'document_type',
              'document_number', 'age']
    success_url = reverse_lazy('users')


class userDeleteView(DeleteView):
    model = User
    template_name = 'library/user/user_delete.html'
    fields = ['first_name', 'last_name', 'document_type',
              'document_number', 'age']
    success_url = reverse_lazy('users')
