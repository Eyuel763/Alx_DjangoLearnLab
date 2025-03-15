# Advanced API Project

## Overview
This project is an advanced Django REST Framework API setup that handles CRUD operations for `Book` models using generic views and custom serializers. It also includes advanced query capabilities such as filtering, searching, and ordering.

## Views Configuration

### BookListView
- **URL:** `/api/books/`
- **Methods:** `GET`, `POST`
- **Description:** Retrieves all books and allows creation of new books. Supports filtering, searching, and ordering.
- **Permission:** `IsAuthenticatedOrReadOnly`
- **Filtering:** Supports filtering by `title`, `author__name`, and `publication_year`.
- **Searching:** Supports searching by `title` and `author__name`.
- **Ordering:** Supports ordering by `title` and `publication_year`.

## Filtering, Searching, and Ordering

### Filtering
To filter the books, use query parameters in the URL. For example:
- Filter by title:
  ```
  /api/books/?title=SomeBookTitle
  ```
- Filter by author name:
  ```
  /api/books/?author__name=AuthorName
  ```
- Filter by publication year:
  ```
  /api/books/?publication_year=2025
  ```

### Searching
To search for books by title or author name, use the `search` query parameter. For example:
```
/api/books/?search=SomeSearchTerm
```

### Ordering
To order the books, use the `ordering` query parameter. For example:
- Order by title:
  ```
  /api/books/?ordering=title
  ```
- Order by publication year:
  ```
  /api/books/?ordering=publication_year
  ```

## Testing
To test the API endpoints, you can use tools like Postman or curl. Ensure to test the following:
- Filtering, searching, and ordering of `Book` instances.

```sh
# Example curl commands
curl -X GET "http://127.0.0.1:8000/api/books/?title=SomeBookTitle"
curl -X GET "http://127.0.0.1:8000/api/books/?author__name=AuthorName"
curl -X GET "http://127.0.0.1:8000/api/books/?publication_year=2025"
curl -X GET "http://127.0.0.1:8000/api/books/?search=SomeSearchTerm"
curl -X GET "http://127.0.0.1:8000/api/books/?ordering=title"
curl -X GET "http://127.0.0.1:8000/api/books/?ordering=publication_year"
```