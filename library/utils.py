from django.shortcuts import redirect, get_object_or_404
from accounts.models import CustomUser
from library.models import Books, BorrowBooks
from django.utils import timezone


def take_return_book(request):
    if request.method == 'POST':
        book_id = request.POST.get('book_id')
        action = request.POST.get('action')

        book = get_object_or_404(Books, id=book_id)

        if action == 'borrow':
            book.borrowed_by = get_object_or_404(CustomUser, id=request.user.id)
            book.save()
        elif action == 'return':
            book.borrowed_by = None
            book.save()

        return redirect('book_list')


def borrowed_book(request, book):
    if not book.borrowed_by:
        book.borrowed_by = request.user
        book.borrowed_date = timezone.now().date()
        book.save()

    BorrowBooks.objects.create(
        book=book,
        user=request.user)