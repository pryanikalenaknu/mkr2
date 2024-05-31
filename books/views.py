from django.shortcuts import render
from books.models import Book, Author

def book_order(request):
    books = Book.objects.all().order_by('-title')
    context = {'books': books}
    return render(request, 'book_list_ordered.html', context)

def book_list(request):
    Book.objects.create(title="Test1", description="Test", price=12, publication_date=datetime.now(), cover_image="test.png")
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'book_list.html', context)

def author_list(request):
    Author.objects.create(name="Test1", bio="Test2")
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
