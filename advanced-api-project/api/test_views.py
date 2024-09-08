from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from .serializers import BookSerializer

class BookAPITestCase(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        
        # Create an author and a book
        self.author = Author.objects.create(name="Author Name")
        self.book = Book.objects.create(
            title="Book Title",
            publication_year=2021,
            author=self.author
        )
        
        # Define URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})
    
    def test_create_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.pk
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(pk=response.data['id']).title, 'New Book')

    def test_create_book_unauthenticated(self):
        data = {
            'title': 'New Book',
            'publication_year': 2023,
            'author': self.author.pk
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Assuming authentication is required

    def test_get_book_list_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_get_book_list_unauthenticated(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)  # Assuming authentication is required

    def test_update_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2022
        }
        response = self.client.put(self.update_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_delete_book_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.list_url, {'title': 'Book Title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.list_url, {'search': 'Book'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books_authenticated(self):
        self.client.login(username='testuser', password='testpassword')
        response = self.client.get(self.list_url, {'ordering': 'title'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], self.book.title)

    def test_permissions(self):
        # Implement tests for permission checks if necessary
        pass
