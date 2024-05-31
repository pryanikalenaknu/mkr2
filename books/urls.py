from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('books/', views.books, name='books'),
    path('authors/', views.authors, name='authors'),
    path('books/book_detail/<int:id>', views.book_detail, name='book_detail'),
    path('authors/author_detail/<int:id>', views.author_detail, name='author_detail'),
    path('books/ordered', views.books_ordered, name='books_ordered')
]
