from django.contrib import admin
from accounts.models import CustomUser, UserReader, UserLibrarian


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'public_id', 'email', 'first_name', 'last_name', 'is_staff']


@admin.register(UserReader)
class UserReaderAdmin(admin.ModelAdmin):
    list_display = ['user',  'address']


@admin.register(UserLibrarian)
class UserLibrarianAdmin(admin.ModelAdmin):
    list_display = ['user',  'personal_number']
