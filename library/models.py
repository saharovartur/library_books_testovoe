from django.db import models
from simple_history.models import HistoricalRecords
from accounts.models import CustomUser


class Genre(models.Model):
    """Модель жанров"""
    name = models.CharField(max_length=200, verbose_name='Жанр')

    class Meta:
        verbose_name = 'Жанр'
        verbose_name_plural = 'Жанры'

    def __str__(self):
        return self.name


class Books(models.Model):
    """Модель книг"""
    name = models.CharField(max_length=200, verbose_name='Название')
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE, verbose_name='Жанр')
    author = models.CharField(max_length=200, verbose_name='Автор')
    description = models.TextField(verbose_name='Описание')
    isbn = models.CharField(max_length=13, verbose_name='ISBN книги', unique=True)
    borrowed_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,
                                    blank=True, verbose_name='Книгу взял')
    history = HistoricalRecords()

    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        ordering = ['name']

    def __str__(self):
        return self.name


class BorrowBooks(models.Model):
    """Модель взятых книг"""

    DRAFT = None

    class Status(models.TextChoices):
        """Класс управления статусами книг."""

        IN_LIBRARY = 'IL', 'В библиотеке'
        ON_HANDS = 'OH', 'На руках'
        RETURN = 'RT', 'Вернул'

    book = models.ForeignKey(Books, on_delete=models.CASCADE, verbose_name='Книга')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name='Пользователь')
    date = models.DateField(auto_now_add=True, verbose_name='Дата')
    status = models.CharField(max_length=3,
                              choices=Status.choices,
                              default=Status.IN_LIBRARY,
                              help_text='Статус книги',
                              verbose_name='Статус')

    def save(self, *args, **kwargs):
        if not self.pk:  # Если это новая запись
            self.status = self.Status.ON_HANDS  # Устанавливаем статус "На руках"
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Взятая книга'
        verbose_name_plural = 'Взятые книги'
        ordering = ['-date']

    def days_on_hand(self):
        from datetime import date
        return (date.today() - self.date).days