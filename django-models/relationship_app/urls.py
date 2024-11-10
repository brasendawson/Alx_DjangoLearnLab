from django.urls import path
from . import views
from .views import list_books
from .views import user_login, user_logout, UserRegisterView
from django.contrib.auth.views import LoginView 
from django.contrib.auth.views import LogoutView 

urlpatterns = [
    # URL pattern for the function-based view to list books
    path('books/', views.list_books, name='list_books'),

    # URL pattern for the class-based view to show library details
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),

    # URL pattern for the login view (using Django's built-in LoginView)
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # URL pattern for the logout view (using Django's built-in LogoutView)
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # URL pattern for the registration view (using the UserRegisterView class-based view)
    path('register/', views.UserRegisterView.as_view(), name='register'),
]
