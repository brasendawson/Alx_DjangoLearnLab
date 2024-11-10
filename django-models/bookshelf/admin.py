from django.contrib import admin

from .models import Book

# Register the Book model
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Customize the list display to show specific fields
    list_display = ('title', 'author', 'publication_year')
    # Add filters for easy navigation
    list_filter = ('publication_year', 'author')
    # Enable search functionality for specific fields
    search_fields = ('title', 'author')

# Register your models here.
