from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User, Role

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    list_display = ('first_name', 'email', 'is_active', 'is_staff', 'role', 'gender', 'phone')
    search_fields = ('first_name', 'email')
    list_filter = ('is_active', 'is_staff')
    ordering = ('-id',)
    list_per_page = 20

    fieldsets = (
        (None, {
            'fields': ('first_name', 'email', 'password', 'date_birth', 'role', 'clinics', 'address', 'gender', 'cpf', 'phone')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'email', 'password1', 'password2'),
        }),
    )

    def save_model(self, request, obj, form, change):
        if not change:  # apenas ao criar novo usuário
            obj.role =  Role.objects.get(name='ADMIN')
        super().save_model(request, obj, form, change)