<<<<<<< HEAD
from django.contrib import admin
from django.urls import path, include
from .views import BookList
from rest_framework.routers import DefaultRouter
from .views import BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# Create router and register viewsets
#router = DefaultRouter()
#router.register(r'books', BookViewSet, basename='book')

# Define URL patterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # Include router URLs
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
=======
from django.urls import path
from .views import BookList

urlpatterns = [
>>>>>>> 3de065d1c0fe3d16e1bfd7e88e15046a08d13ff0
    path('books/', BookList.as_view(), name='book-list'),
]
