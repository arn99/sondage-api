from django.contrib import admin

from sondageapp.models import CustomUser, Inquiry, Question, Questionnaire, Response, Customer
from django.contrib.auth.admin import UserAdmin
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_commercial', 'code_commercial')
        })
    )
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
     'is_commercial', 'code_commercial'
        )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permissions', {
            'fields': (
                'is_active', 'is_staff', 'is_superuser',
                'groups', 'user_permissions'
                )
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        }),
        ('Additional info', {
            'fields': ('is_commercial', 'code_commercial')
        })
    )
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Inquiry)
admin.site.register(Questionnaire)
admin.site.register(Response)
admin.site.register(Question)
admin.site.register(Customer)