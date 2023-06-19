from django.urls import path


from .views import authors, books, users, views


urlpatterns = [
    path('', views.index, name="index")
]

urlpatterns += [
    path("book/", books.bookListView.as_view(), name="books"),
    path("book/<int:pk>/", books.bookDetailView.as_view(), name='book-detail'),
    path("book/create/", books.bookCreateView.as_view(), name='create-book'),
    path('book/<int:pk>/edit/', books.bookEditView.as_view(), name='book-edit'),
    path('book/<int:pk>/delete/', books.bookDeleteView.as_view(), name='book-delete'),
    path("user/", users.userListView.as_view(), name="users"),
    path("user/<int:pk>/", users.userDetailView.as_view(), name='user-detail'),
    path("user/create/", users.userCreateView.as_view(), name='create-user'),
    path('user/<int:pk>/edit/', users.userEditView.as_view(), name='user-edit'),
    path('user/<int:pk>/delete/', users.userDeleteView.as_view(), name='user-delete'),
    path('author/', authors.authorListView.as_view(), name='authors'),
    path('author/<int:pk>/', authors.authorDetailView.as_view(), name='author-detail'),
    path('author/create/', authors.authorCreateView.as_view(), name='create-author'),
    path('author/<int:pk>/edit/', authors.authorEditView.as_view(), name='author-edit'),
    path('author/<int:pk>/delete/', authors.authorDeleteView.as_view(), name='author-delete'),
]

