from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from api.serializers import BookSerializers, BorrowBooksSerializers
from library.models import Books, BorrowBooks


class BookList(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BookSerializers


class BorrowBooksList(generics.ListAPIView):
    queryset = BorrowBooks.objects.all()
    serializer_class = BorrowBooksSerializers
    permission_classes = [IsAuthenticated]






