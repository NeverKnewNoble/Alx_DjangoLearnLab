## API Endpoints and View Configurations

The following endpoints provide CRUD functionality for managing the `Book` and `Author` models.

### Book Views

1. **List View (Retrieve All Books)**

   **URL:** `/api/books/`  
   **Method:** `GET`  
   **View:** `BookListView`  
   **Description:**  
   - Returns a list of all books.
   - Available to unauthenticated users (read-only).
   - Requires `IsAuthenticatedOrReadOnly` permission for security.
   
2. **Detail View (Retrieve a Single Book)**

   **URL:** `/api/books/<int:pk>/`  
   **Method:** `GET`  
   **View:** `BookDetailView`  
   **Description:**  
   - Returns detailed information for a single book.
   - Available to unauthenticated users (read-only).

3. **Create View (Add a New Book)**

   **URL:** `/api/books/create/`  
   **Method:** `POST`  
   **View:** `BookCreateView`  
   **Description:**  
   - Allows an authenticated user to add a new book.
   - Uses `IsAuthenticated` permission to ensure only logged-in users can create books.
   - Validates the `publication_year` to ensure it is not set in the future.

4. **Update View (Modify an Existing Book)**

   **URL:** `/api/books/<int:pk>/update/`  
   **Method:** `PUT`, `PATCH`  
   **View:** `BookUpdateView`  
   **Description:**  
   - Allows an authenticated user to modify an existing book's information.
   - Uses `IsAuthenticated` permission for security.
   - Validation for `publication_year` ensures correct data handling.

5. **Delete View (Remove a Book)**

   **URL:** `/api/books/<int:pk>/delete/`  
   **Method:** `DELETE`  
   **View:** `BookDeleteView`  
   **Description:**  
   - Allows an authenticated user to delete a book.
   - Uses `IsAuthenticated` permission to ensure that only authorized users can delete a book.


## API Query Parameters

### Filtering
You can filter books by title, author, and publication year:
- `/api/books/?title=exampletitle`
- `/api/books/?author=authorname`
- `/api/books/?publication_year=2022`

### Searching
You can search books by title or author:
- `/api/books/?search=exampletitle`
- `/api/books/?search=authorname`

### Ordering
You can order books by title or publication year:
- `/api/books/?ordering=title`
- `/api/books/?ordering=-publication_year` (for descending order)
