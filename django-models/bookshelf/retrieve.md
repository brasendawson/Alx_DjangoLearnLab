### Retrieve Operation
Command:
```python
retrieved_book = Book.objects.get(title="1984")
print("Retrieved book:", retrieved_book)