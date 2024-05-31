from django.shortcuts import render
from books.models import Book, Author

def books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)

def authors(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'author_list.html', context)

def book_details(request, id):
    book = get_object_or_404(Book, id=id)
    context = {'book': book}
    return render(request, 'book_detail.html', context)
