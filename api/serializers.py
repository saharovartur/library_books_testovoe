from rest_framework import serializers
from library.models import Books, BorrowBooks


class BookSerializers(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = ('name', 'author', 'genre')


class BorrowBooksSerializers(serializers.ModelSerializer):
    class Meta:
        model = BorrowBooks
        fields = ('book', 'user', 'date', 'status')

