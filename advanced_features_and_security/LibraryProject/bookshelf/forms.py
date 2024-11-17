from django import forms
from .models import Book

# ExampleForm or BookForm - Modify according to your use case
class ExampleForm(forms.Form):  # Or BookForm(forms.ModelForm)
    title = forms.CharField(max_length=255)
    author = forms.CharField(max_length=255)

    def clean_title(self):
        title = self.cleaned_data['title']
        # Add further validation logic if needed
        return title