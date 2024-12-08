from django.db import models
from django.contrib.auth.models import User

class Author(models.Model): # The Author model represents a writer with a one-to-many relationship to books.
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model): # The Book model contains details about books, each linked to an Author.
    title = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
