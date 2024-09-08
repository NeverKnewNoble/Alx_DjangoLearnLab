from django.db import models

# The Author model represents the book's author. Each author can have multiple books.
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# The Book model represents a single book with a title, publication year, and an author.
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
