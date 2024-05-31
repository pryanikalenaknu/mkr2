from django.shortcuts import render
from books.models import Book, Author

def books(request):
    books = Book.objects.all()
    context = {'title': 'Books', 'books': books}
    return render(request, 'book_list.html', context)
