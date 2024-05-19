from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, UserProfile
from django.contrib.auth.models import Group


class UserProfileInline(admin.StackedInline):
    model = UserProfile


class UserAdmin(BaseUserAdmin):

    list_display = ('email', 'phone_number', 'is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        ('change info', {'fields': ('email', 'phone_number', 'full_name', 'password')}),
        ('Permissions', {'fields':('is_active', 'is_admin', 'last_login')})
    )

    add_fieldsets = (
        (None, {'fields':('email', 'phone_number', 'full_name', 'password1', 'password2')}),
    )

    inlines = (UserProfileInline,)
    search_fields = ('email', 'full_name')
    ordering = ('full_name',)
    filter_horizontal = ()



admin.site.unregister(Group)
admin.site.register(User, UserAdmin)