from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .models import Book
from .serializers import BookSerializer
from rest_framework import generics

<<<<<<< HEAD
#class BookViewSet(viewsets.ModelViewSet):
=======
>>>>>>> 3de065d1c0fe3d16e1bfd7e88e15046a08d13ff0
class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated] 
