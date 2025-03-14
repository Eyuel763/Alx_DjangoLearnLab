# Advanced API Project

## Overview
This project is an advanced Django REST Framework API setup that handles CRUD operations for `Book` models using generic views and custom serializers.

## Views Configuration

### BookListView
- **URL:** `/books/`
- **Methods:** `GET`
- **Description:** Retrieves all books. Allows read-only access to unauthenticated users.
- **Permission:** `IsAuthenticatedOrReadOnly`

### BookDetailView
- **URL:** `/books/<int:pk>/`
- **Methods:** `GET`
- **Description:** Retrieves a single book by ID. Allows read-only access to unauthenticated users.
- **Permission:** `IsAuthenticatedOrReadOnly`

### BookCreateView
- **URL:** `/books/create/`
- **Methods:** `POST`
- **Description:** Adds a new book. Restricted to authenticated users only.
- **Permission:** `IsAuthenticated`

### BookUpdateView
- **URL:** `/books/<int:pk>/update/`
- **Methods:** `PUT`
- **Description:** Modifies an existing book. Restricted to authenticated users only.
- **Permission:** `IsAuthenticated`

### BookDeleteView
- **URL:** `/books/<int:pk>/delete/`
- **Methods:** `DELETE`
- **Description:** Removes a book. Restricted to authenticated users only.
- **Permission:** `IsAuthenticated`

## Testing
To test the API endpoints, you can use tools like Postman or curl. Ensure to test the following:
- Creation, retrieval, update, and deletion of `Book` instances.
- Permissions enforcement by accessing endpoints with and without proper credentials.

```sh
# Example curl commands
curl -X GET http://127.0.0.1:8000/books/
curl -X GET http://127.0.0.1:8000/books/1/
curl -X POST http://127.0.0.1:8000/books/create/ -d '{"title":"New Book", "publication_year":2025, "author":1}'
curl -X PUT http://127.0.0.1:8000/books/1/update/ -d '{"title":"Updated Book"}'
curl -X DELETE http://127.0.0.1:8000/books/1/delete/
```

## Notes
- Ensure you have created a superuser to access the Django admin interface.
- Use the admin interface to manage `Author` and `Book` instances if needed.
