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

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['body']
    fields = ['body']
    list_filter = ['body']
    search_fields = ['body']
class ResponseAdmin(admin.ModelAdmin):
    def question_body(self, obj):
        return obj.question.body
    list_display = ('choice', 'question_body')
    fields = ('choice', 'question')
    list_filter = ('choice', 'question')
    autocomplete_fields = ['question']

    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Inquiry)
admin.site.register(Questionnaire)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Customer)