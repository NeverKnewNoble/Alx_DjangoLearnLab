# delete.md

```python
from bookshelf.models import Book

book = Book.objects.get(id=1)
book.delete()

# Verify deletion
books = Book.objects.all()
print(books)
# Expected output: <QuerySet []>
