# retrieve.md

```python
book = Book.objects.get(id=1)
print(book.title, book.author, book.publication_year)
# Expected output: 1984 George Orwell 1949
