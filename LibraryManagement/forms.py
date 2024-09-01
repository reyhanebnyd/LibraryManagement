from django import forms
from .models import Book, Author
from django.core.exceptions import ValidationError
import datetime

class BookForm(forms.ModelForm):
    author = forms.ModelChoiceField(queryset=Author.objects.all(), required=False)
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date', 'price']
        widgets = {
            'publication_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_publication_date(self):
        date = self.cleaned_data.get('publication_date')
        if date is None or date.year < 1900:
            raise ValidationError('Please enter a valid publication date.')
        return date


class AuthorForm(forms.ModelForm):  
    class Meta:  
        model = Author  
        fields = ['name']