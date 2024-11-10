import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

author_name = 'J.K. Rowling'
author = Author.objects.filter(name=author_name).first()
if author:
    books_by_author = author.books.all()
    print(f"Books by {author_name}:")
    for book in books_by_author:
        print(f"- {book.title}")
else:
    print(f"No author found with name {author_name}.")

library_name = 'Central Library'
library = Library.objects.filter(name=library_name).first()
if library:
    books_in_library = library.books.all()
    print(f"\nBooks in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title}")
else:
    print(f"No library found with name {library_name}.")

library = Library.objects.filter(name=library_name).first()
if library and hasattr(library, 'librarian'):
    print(f"\nLibrarian for {library_name}: {library.librarian.name}")
else:
    print(f"No librarian found for {library_name}.")
