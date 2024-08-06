import uuid
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, AbstractUser
from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from django.http import Http404


class UserManager(BaseUserManager):
    def get_object_by_public_id(self, public_id):
        try:
            instance = self.get(public_id=public_id)
            return instance
        except (ObjectDoesNotExist, ValueError, TypeError):
            raise Http404("User not found")

    def create_user(self, email, username, password=None, **kwargs):
        """Создадим и вернем юзера с данными"""
        if username is None:
            raise TypeError('Укажите имя')
        if email is None:
            raise TypeError('Укажите email')
        if password is None:
            raise TypeError('Укажите пароль')

        user = self.model(username=username,
                          email=self.normalize_email(email), **kwargs)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password, **kwargs):
        """Создадим и вернем суперпользователя с данными"""
        if password is None:
            raise TypeError('Укажите пароль')
        if email is None:
            raise TypeError('Укажите email')
        if username is None:
            raise TypeError('Укажите имя')

        user = self.create_user(email, username, password, **kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class CustomUser(AbstractBaseUser, PermissionsMixin):
    public_id = models.UUIDField(db_index=True, unique=True,
                                 default=uuid.uuid4, editable=False)
    username = models.CharField(db_index=True, max_length=30, unique=True,
                                verbose_name='Никнейм')
    first_name = models.CharField(max_length=250, verbose_name='Имя')
    last_name = models.CharField(max_length=250, verbose_name='Фамилия')
    email = models.EmailField(db_index=True, unique=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True, verbose_name='Создан')
    updated = models.DateTimeField(auto_now_add=True, verbose_name='Обновлен')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Группы',
        blank=True,
        related_name='custom_user_set'
    )

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='Разрешения пользователя',
        blank=True,
        related_name='custom_user_permissions'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return f"{self.email}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


class UserReader(models.Model):
    """Модель пользователя-читателя"""
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=False)
    address = models.TextField(verbose_name='Адрес проживания')

    class Meta:
        verbose_name = 'Читатель'
        verbose_name_plural = 'Читатели'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'


class UserLibrarian(models.Model):
    """Модель пользователя-библиотекаря"""

    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, null=False)
    personal_number = models.IntegerField(verbose_name='Персональный номер')

    class Meta:
        verbose_name = 'Библиотекарь'
        verbose_name_plural = 'Библиотекари'

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'

