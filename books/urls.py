from django.urls import path

from books import views

app_name = 'books'

urlpatterns = [
    path('books/', views.book_list, name='books'),
    path('authors/', views.author_list, name='authors'),
    path('book_detail/<int:id>', views.book_details, name='book_detail'),
    path('author_detail/<int:id>', views.author_details, name='author_detail'),
]
