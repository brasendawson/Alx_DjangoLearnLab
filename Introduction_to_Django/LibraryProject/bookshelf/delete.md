### Delete Operation
Command:
```python
retrieved_book.delete()
print("Book deleted successfully")

books = Book.objects.all()
print("Books remaining in database:", books)