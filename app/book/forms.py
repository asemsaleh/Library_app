# Import form, our book model
from django import forms
from .models import Book

class BookCreate(forms.ModelForm):
    class Meta:
        model = Book

        # Input from user
        fields = '__all__'