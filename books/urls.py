from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('books/', views.book_list, name='books'),
    path('authors/', views.author_list, name='authors'),
    path('books/book_details/<int:id>', views.book_details, name='book_details'),
    path('authors/author_details/<int:id>', views.author_details, name='author_details'),
    path('books/order', views.book_order, name='book_order'),
]
