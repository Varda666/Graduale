from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'name', 'last_login',
                    'is_staff', 'is_active')
    list_filter = ('email', 'name', 'last_login',
                   'is_staff', 'is_active')
    search_fields = ('email', 'name', 'last_login',
                     'is_staff', 'is_active')


