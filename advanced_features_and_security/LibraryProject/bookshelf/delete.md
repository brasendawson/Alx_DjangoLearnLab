### Delete Operation
Command:
```python
from bookshelf.models import Book

# Retrieve the book to delete
retrieved_book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
retrieved_book.delete()
print("Book deleted successfully")

# Confirm deletion
books = Book.objects.all()
print("Books remaining in database:", books)
