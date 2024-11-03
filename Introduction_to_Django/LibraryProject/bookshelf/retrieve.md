from bookshelf.models import Book
# Retrieve the book
book = Book.objects.get(pk=1)  # Replace 1 with the actual ID

# Expected Output: Shows all attributes of the created book
print(book)