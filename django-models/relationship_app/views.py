from django.shortcuts import render
from .views import list_books
from .models import Book
from django.views.generic.detail import DetailView

# Function-Based View to list all books
def list_books(request):
    # Get all books from the database
    books = Book.objects.all()

    # Render the 'list_books.html' template, passing the books context
    return render(request, 'relationship_app/list_books.html', {'books': books})

from django.views.generic import DetailView
from .models import Library

# Class-Based View to show details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # To use 'library' in the template context


# Create your views here.
