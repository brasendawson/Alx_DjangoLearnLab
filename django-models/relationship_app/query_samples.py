import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # Make sure 'myproject' is your actual project name
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def get_books_by_author(author_name):
    try:

        author = Author.objects.get(name=author_name)
        
        books_by_author = Book.objects.filter(author=author)
        
        if books_by_author.exists():
            print(f"Books by {author_name}:")
            for book in books_by_author:
                print(f"- {book.title}")
        else:
            print(f"{author_name} has not written any books.")
    except Author.DoesNotExist:
        print(f"No author found with the name '{author_name}'.")


def list_books_in_library(library_name):
    try:
        library = Library.objects.get(name=library_name)
        books_in_library = library.books.all()
        print(f"\nBooks in {library_name}:")
        for book in books_in_library:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")


def get_librarian_for_library(library_name):
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        
        librarian = Librarian.objects.get(library=library)
        
        print(f"\nLibrarian for {library_name}: {librarian.name}")
    except Library.DoesNotExist:
        print(f"No library found with the name '{library_name}'.")
    except Librarian.DoesNotExist:
        print(f"No librarian assigned to {library_name}.")

