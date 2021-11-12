from django.urls import path

from .views import CustomerCreateApi, CustomerListApi, CustomerUpdateApi, HelloView, CustomUserCreateApi, CustomUserListApi, CustomUserUpdateApi, InquiryCreateApi, InquiryListApi, InquiryUpdateApi, QuestionCreateApi, QuestionListApi, QuestionUpdateApi, QuestionnaireCreateApi, QuestionnaireListApi, QuestionnaireUpdateApi, RegisterApi, ResponseCreateApi, ResponseListApi, ResponseUpdateApi

urlpatterns = [
    path('api/user/create',CustomUserCreateApi.as_view()),
    path('api/user',CustomUserListApi.as_view()),
    path('api/user/<int:pk>',CustomUserUpdateApi.as_view()),
    path('api/inquiry/create',InquiryCreateApi.as_view()),
    path('api/inquiry',InquiryListApi.as_view()),
    path('api/inquiry/<int:pk>',InquiryUpdateApi.as_view()),
    path('api/question/create',QuestionCreateApi.as_view()),
    path('api/question',QuestionListApi.as_view()),
    path('api/question/<int:pk>',QuestionUpdateApi.as_view()),
    path('api/response/create',ResponseCreateApi.as_view()),
    path('api/response',ResponseListApi.as_view()),
    path('api/response/<int:pk>',ResponseUpdateApi.as_view()),
    path('api/questionnaire/create',QuestionnaireCreateApi.as_view()),
    path('api/questionnaire',QuestionnaireListApi.as_view()),
    path('api/questionnaire/<int:pk>',QuestionnaireUpdateApi.as_view()),
    path('api/client/create',CustomerCreateApi.as_view()),
    path('api/client',CustomerListApi.as_view()),
    path('api/client/<int:pk>',CustomerUpdateApi.as_view()),
    path('api/hello/', HelloView.as_view(), name='hello'),
    path('api/register', RegisterApi.as_view()),
]