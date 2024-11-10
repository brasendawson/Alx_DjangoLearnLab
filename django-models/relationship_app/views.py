from django.shortcuts import render, redirect
from django.contrib.auth import login, logout  # Import login and logout functions
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm  # Import authentication and user creation forms
from django.views.generic import DetailView, CreateView  # Import generic views
from django.urls import reverse_lazy
from .models import Book, Library  # Import models for Book and Library

# Function-Based View to list all books
def list_books(request):
    books = Book.objects.all()  # Retrieve all books from the database
    return render(request, 'relationship_app/list_books.html', {'books': books})  # Render the list_books template with books

# Class-Based View to show details for a specific library
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'  # To use 'library' as the context name in the template

# Login view using Django's built-in LoginView
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)  # Log the user in
            return redirect('home')  # Redirect to a protected view (replace 'home' with actual URL name)
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# Logout view using Django's built-in LogoutView
def user_logout(request):
    logout(request)  # Log the user out
    return render(request, 'relationship_app/logout.html')  # Render logout confirmation page

# Registration view for creating new users
class UserRegisterView(CreateView):
    form_class = UserCreationForm  # Use the built-in UserCreationForm for registration
    template_name = 'relationship_app/register.html'
    success_url = reverse_lazy('login')  # Redirect to the login page after successful registration
