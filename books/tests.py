from django.test import TestCase
from .models import Author, Book
from datetime import date
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile

from books.models import Book, Author

class ModelTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(name='Test Author', bio='Test Bio')
        Book.objects.create(title='Test Book', description='Test Description',
                            publication_date=date.today(), cover_image=SimpleUploadedFile('test_image.jpg', b'content'), price=10.00)
        book = Book.objects.get(id=1)
        book.authors.add(author)

    def test_author_str(self):
        author = Author.objects.get(id=1)
        self.assertEqual(str(author), 'Test Author')

    def test_book_str(self):
        book = Book.objects.get(id=1)
        self.assertEqual(str(book), 'Test Book')

    def test_book_authors(self):
        book = Book.objects.get(id=1)
        authors = book.authors.all()
        self.assertTrue(authors.exists())

    def test_book_publication_date(self):
        book = Book.objects.get(id=1)
        publication_date = book.publication_date
        self.assertEqual(publication_date, date.today())

    def test_book_price(self):
        book = Book.objects.get(id=1)
        price = book.price
        self.assertEqual(price, 10.00)

    def test_author_detail_view(self):
        response = self.client.get("/authors/author_detail/1")
        self.assertEqual(response.status_code, 200)

    def test_book_detail_view(self):
        response = self.client.get("/books/book_detail/1")
        self.assertEqual(response.status_code, 200)
