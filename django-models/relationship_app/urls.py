from django.urls import path
from .views import list_books, LibraryDetailView, register  # Ensure 'register' is imported
from django.contrib.auth import views as auth_views
from .views import add_book, edit_book, delete_book

urlpatterns = [
     path('books/add/', views.add_book, name='add_book/'),
    path('books/<pk>/edit/', views.edit_book, name='edit_book/'),
    path('books/<pk>/delete/', views.delete_book, name='delete_book'),
    path('admin-view/', views.admin_view, name='admin_view'),
    path('librarian-view/', views.librarian_view, name='librarian_view'),
    path('member-view/', views.member_view, name='member_view'),
     path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', views.home, name='home')
    
     ]
