from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('books', views.books, name='books'),
    path('authors', views.authors, name='authors')
]
