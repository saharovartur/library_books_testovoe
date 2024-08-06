from django.urls import path
from .views import BookList, BorrowBooksList

urlpatterns = [
    path("book-list/", BookList.as_view(), name="book_list"),
    path("borrow-book/", BorrowBooksList.as_view(), name="book_list"),


]