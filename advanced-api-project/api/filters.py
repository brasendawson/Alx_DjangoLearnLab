import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    # Assuming 'author' is a ForeignKey to an Author model with a 'name' field
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')

    class Meta:
        model = Book
        fields = ['title', 'author_name', 'publication_year']  # Include the new filter field