from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Author
from django.contrib.auth.models import User
from django_filters import rest_framework
from rest_framework.filters import OrderingFilter
from rest_framework.filters import SearchFilter
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from .filters import BookFilter
from rest_framework import filters

class BookAPITestCase(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')

        # Initialize APIClient and authenticate
        self.client = APIClient()
        self.client.login(username='testuser', password='testpassword')

        # Create Author and Book instances
        self.author = Author.objects.create(name="Author Name")
        self.book = Book.objects.create(title="Book Title", publication_year=2023, author=self.author)

        # Define endpoints
        self.list_url = '/api/books/'
        self.detail_url = f'/api/books/{self.book.id}/'

    def tearDown(self):
        self.client.logout()

    # Test listing all books
    def test_list_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Book Title")

    # Test retrieving a single book
    def test_retrieve_book(self):
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Book Title")

    # Test creating a new book
    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2024,
            "author": self.author.id
        }
        response = self.client.post(self.list_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    # Test updating an existing book
    def test_update_book(self):
        data = {
            "title": "Updated Book",
            "publication_year": 2023,
            "author": self.author.id
        }
        response = self.client.put(self.detail_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Updated Book")

    # Test deleting a book
    def test_delete_book(self):
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # Test unauthenticated access
    def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [filters.OrderingFilter]
    filter_backends = [filters.SearchFilter]
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = BookFilter
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year', 'author__name']  # Specify the fields that can be used for ordering
    ordering = ['title']  # Default ordering