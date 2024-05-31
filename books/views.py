from django.shortcuts import render
from books.models import Book, Author

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)

def author_list(request):
    authors = Author.objects.all()
    context = {'authors': authors}
    return render(request, 'author_list.html', context)

def book_details(request, id):
    book = get_object_or_404(Book, id=id)
    context = {'book': book}
    return render(request, 'book_detail.html', context)

def author_details(request, id):
    author = get_object_or_404(Author, id=id)
    context = {'author': author}
    return render(request, 'author_detail.html', context)
