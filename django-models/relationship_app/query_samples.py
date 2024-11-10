import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # Make sure 'myproject' is your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# 1. Query all books by a specific author
def get_books_by_author(author_name):
    try:
        author = Author.objects.get(name=author_name)
        books_by_author = author.books.all()
        print(f"Books by {author_name}:")
        for book in books_by_author:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'.")


# 2. List all books in a specific library
def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")


# 3. Retrieve the librarian for a specific library
def get_librarian_for_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        if hasattr(library, 'librarian'):
            print(f"\nLibrarian for {library_name}: {library.librarian.name}")
        else:
            print(f"No librarian assigned to {library_name}.")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")
