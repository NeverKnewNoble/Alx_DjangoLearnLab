from django.urls import path
from .views import list_books, LibraryDetailView, register  # Ensure 'register' is imported
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('register/', views.register, name='register'),
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),
    path('', views.home, name='home')
]
