from django.urls import path
from . import views
from .views import list_books

urlpatterns = [
    # URL pattern for the function-based view to list books
    path('books/', views.list_books, name='list_books'),

    # URL pattern for the class-based view to show library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
]