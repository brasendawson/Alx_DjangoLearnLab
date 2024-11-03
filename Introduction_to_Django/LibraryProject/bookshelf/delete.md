from bookshelf.models import Book

# Delete the book
book.delete()

# Confirm deletion (should raise an error)
books = Book.objects.all()
print(books)