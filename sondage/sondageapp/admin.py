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
    def inquiry_title(self, obj):
        return obj.inquiry.title
    list_display = ('body','inquiry_title')
    fields = ('body','inquiry', 'date_created')
    fields = ('body','inquiry', 'date_created')
    list_filter = ('body','inquiry')
    search_fields = ['body']
class ResponseAdmin(admin.ModelAdmin):
    def question_body(self, obj):
        return obj.question.body
    list_display = ('choice', 'type', 'question_body')
    fields = ('choice', 'type', 'question','date_created')
    list_filter = ('choice', 'question')
    autocomplete_fields = ['question']

class QuestionnaireAdmin(admin.ModelAdmin):
    def questions_body(self, obj):
        return obj.questions.body
    def responses_choice(self, obj):
        return obj.responses.choice
    def responses_type(self, obj):
        return obj.responses.type
    list_display = ('questions_body','responses_choice', 'responses_type', 'other')
    fields = ('responses', 'questions','date_created', 'other')
    list_filter = ('responses', 'questions', 'other')
    autocomplete_fields = ['questions']
    search_fields = ['responses__choice']
class InquiryAdmin(admin.ModelAdmin):
    list_display = ('title', )
    fields = ('title', 'date_created')
    list_filter = ('title', )
    search_fields = ['title']
    
    
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(Questionnaire, QuestionnaireAdmin)
admin.site.register(Response, ResponseAdmin)
admin.site.register(Customer)