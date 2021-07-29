from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


class UserAdmin(UserAdmin):
    fieldsets = (
        ('System credentials', {'fields': ('username', 'password')}),
        ('Premissions', {'fields': ('role',)})
    )


admin.site.register(User, UserAdmin)
