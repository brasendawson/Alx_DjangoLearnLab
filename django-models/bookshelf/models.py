from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()  # Ensure this is defined as a field

    def __str__(self):
        return f"{self.title} by {self.author}"

# Create your models here.