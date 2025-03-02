from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date', 'isbn', 'summary']

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if "<script>" in title:
            raise forms.ValidationError("Invalid input detected!")
        return title

    def clean_summary(self):
        summary = self.cleaned_data.get("summary")
        if "<script>" in summary:
            raise forms.ValidationError("Invalid input detected!")
        return summary
