from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book
from django.http import HttpResponse
from .forms import BookForm


@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    return render(request, 'bookshelf/book_detail.html', {'book': book})

@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # logic to create a book
        pass
    return render(request, 'bookshelf/book_form.html')

@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # logic to edit the book
        pass
    return render(request, 'bookshelf/book_form.html', {'book': book})

@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        # logic to delete the book
        book.delete()
        return redirect('bookshelf:book_list')
    return render(request, 'bookshelf/book_confirm_delete.html', {'book': book})


# Example view with Django ORM to prevent SQL injection
def search_books(request):
    query = request.GET.get('query', '')
    if query:
        books = Book.objects.filter(title__icontains=query)  # Safe query using ORM
    else:
        books = Book.objects.all()  # Show all books if no query
    return render(request, 'book_list.html', {'books': books})

# Example form validation
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('Book added successfully')
    else:
        form = BookForm()
    return render(request, 'add_book.html', {'form': form})

# Create your views here.
