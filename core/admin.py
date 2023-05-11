from django.contrib import admin

from core.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'last_name')
    search_fields = ('username', 'first_name', 'last_name')
    readonly_fields = ('last_login',)
    exclude = ['password', 'user_permissions', 'groups', 'is_superuser']
    empty_value_display = '-empty-'
