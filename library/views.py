from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from library.models import Books, BorrowBooks
from library.utils import take_return_book, borrowed_book, borrowed_book


def home_view(request):
    return render(request, 'home.html')


class MyBookList(ListView):
    """Вью списка взятых книг 'Мои книги'"""
    model = BorrowBooks
    template_name = 'books/my_book_list.html'

    def get_queryset(self):
        return BorrowBooks.objects.filter(user=self.request.user)


def book_list(request):
    """Вью списка всех книг
    с возможностью взять или вернуть книги"""
    books = Books.objects.all().order_by('name')

    take_return = take_return_book(request)

    return render(request, 'books/book_list.html', {'books': books})


def borrow_book(request, book_id):
    """Вью взятия книги"""
    book = get_object_or_404(Books, id=book_id)

    borrow_book = borrowed_book(request, book)

    return redirect('book_list')


def overdue_books_list(request):
    """Вью списка должников
    в спике те у кого книга на руках по статусу в модели"""
    overdue_issues = BorrowBooks.objects.filter(status=BorrowBooks.Status.ON_HANDS)
    context = {
        'overdue_issues': overdue_issues,
    }
    return render(request, 'borrowers_list.html', context)