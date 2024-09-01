from django.contrib import admin
from .models import Book
<<<<<<< HEAD
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
=======
>>>>>>> 575d54c4aa0fd29d7edaff798bcbc16292a9012c

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    search_fields = ('title', 'author')
    list_filter = ('publication_year',)

<<<<<<< HEAD
=======
    # users/admin.py

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

>>>>>>> 575d54c4aa0fd29d7edaff798bcbc16292a9012c
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'date_of_birth', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('date_of_birth', 'profile_photo')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
