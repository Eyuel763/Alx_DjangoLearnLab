import os
import django

os.environ.setdefault("DJANGO_SETTING_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

#Sample Data Creation
author1 = Author.objects.create(name="Jane Doe")
book1 = Book.objects.create(title="Python Bsics", author=author1)
book2 = Book.objects.create(title="Django Unleashed", author=author1)
library1 = Library.objects.create(name="Central Library")
library1.books.add(book1, book2)
librarian1 = Librarian.objects.create(name="John Smith", library=library1)

# Query all books by a specific author
author_books = Book.objects.filter(author=author1)
print("Books by Jane Doe: ")
for book in author_books:
    print(book.title)

# List all books in a library
library_books = library1.books.all()
print("\nBooks in Central Library:")
for book in library_books:
    print(book.title)

# Retrieve the librarian for a library
library_librarian = Librarian.objects.get(library=library1)
print(f"\nLibrarian for Central Library: {library_librarian.name}")
