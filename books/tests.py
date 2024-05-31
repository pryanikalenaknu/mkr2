from django.test import TestCase
from .models import Author, Book
from datetime import date
from django.core.files.uploadedfile import SimpleUploadedFile


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
