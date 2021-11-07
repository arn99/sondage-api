from django.contrib import admin

from sondageapp.models import Inquiry, Question, Questionnaire, Response, User, Customer

# Register your models here.

admin.site.register(User)
admin.site.register(Inquiry)
admin.site.register(Questionnaire)
admin.site.register(Response)
admin.site.register(Question)
admin.site.register(Customer)