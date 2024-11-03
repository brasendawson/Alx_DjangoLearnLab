from bookshelf.models import Book

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Expected Output: Shows the updated title
print(book)