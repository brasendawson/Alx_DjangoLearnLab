from bookshelf.models import Book

book = Book.objects.get(pk=1)  # Replace 1 with the actual ID

print(book)