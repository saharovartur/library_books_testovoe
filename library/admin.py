from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin

from library.models import Genre, Books,  BorrowBooks


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Books)
class BooksAdmin(SimpleHistoryAdmin):
    list_display = ['name', 'genre', 'author', 'description', 'isbn']


@admin.register(BorrowBooks)
class BorrowBooksAdmin(admin.ModelAdmin):
    list_display = ['id', 'book', 'user', 'date']