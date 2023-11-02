"""
Vistas genericas para administrar los Usuarios
"""
from django.views import generic
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from ..models.users import User


class UserListView(generic.ListView):
    """
    Vista genérica para mostrar una lista de Usuarios.
    """
    model = User
    context_object_name = 'user_list'
    template_name = 'library/user/user_list.html'


class UserDetailView(generic.DetailView):
    """
    Vista genérica para mostrar los detalles de un Usuario.
    """
    model = User
    context_object_name = 'user'
    template_name = 'library/user/user_detail.html'


class UserCreateView(generic.CreateView):
    """
    Vista genérica para crear un nuevo Usuario.
    """
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


class UserEditView(UpdateView):
    """
    Vista genérica para editar los detalles de un usuario existente.
    """
    model = User
    template_name = 'library/user/user_edit.html'
    fields = ['first_name', 'last_name', 'document_type',
              'document_number', 'age']
    success_url = reverse_lazy('users')


class UserDeleteView(DeleteView):
    """
    Vista genérica para eliminar un usuario existente.
    """
    model = User
    template_name = 'library/user/user_delete.html'
    fields = ['first_name', 'last_name', 'document_type',
              'document_number', 'age']
    success_url = reverse_lazy('users')
