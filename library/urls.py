from django.urls import path


from .views import authors, books, users, views


urlpatterns = [
    path('', views.index, name="index")
]

urlpatterns += [
    path("book/", books.BookListView.as_view(), name="books"),
    path("book/<int:pk>/", books.BookDetailView.as_view(), name='book-detail'),
    path("book/create/", books.BookCreateView.as_view(), name='create-book'),
    path('book/<int:pk>/edit/', books.BookEditView.as_view(), name='book-edit'),
    path('book/<int:pk>/delete/', books.BookDeleteView.as_view(), name='book-delete'),
    path('book/books-for-category/<str:category>/', books.books_for_category, name='books-for-category'),
    
    path("user/", users.UserListView.as_view(), name="users"),
    path("user/<int:pk>/", users.UserDetailView.as_view(), name='user-detail'),
    path("user/create/", users.UserCreateView.as_view(), name='create-user'),
    path('user/<int:pk>/edit/', users.UserEditView.as_view(), name='user-edit'),
    path('user/<int:pk>/delete/', users.UserDeleteView.as_view(), name='user-delete'),
    path('author/', authors.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>/', authors.AuthorDetailView.as_view(), name='author-detail'),
    path('author/create/', authors.AuthorCreateView.as_view(), name='create-author'),
    path('author/<int:pk>/edit/',
         authors.AuthorEditView.as_view(), name='author-edit'),
    path('author/<int:pk>/delete/',
         authors.AuthorDeleteView.as_view(), name='author-delete'),
]
