from django.urls import path
from library import views
from library.views import MyBookList

urlpatterns = [
    path('books/', views.book_list, name='book_list'),
    path('books/borrow/<int:book_id>/', views.borrow_book, name='borrow_book'),
    path('', views.home_view, name='home'),
    path('mybooklist/', MyBookList.as_view(), name='mybooklist'),
    path('borrowers-list/', views.overdue_books_list, name='borrowers-list'),

]
