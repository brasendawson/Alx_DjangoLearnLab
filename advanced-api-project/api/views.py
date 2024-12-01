from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import SearchFilter
from rest_framework.filters import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
from rest_framework import generics

class BookListCreateView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  
    
    filterset_fields = ['title', 'author__name', 'publication_year']
    
    # Specify the fields available for searching
    search_fields = ['title', 'author__name']
    
    # Specify the fields available for ordering
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # Default ordering