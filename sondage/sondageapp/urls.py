from django.urls import path

from .views import CustomerCreateApi, CustomerListApi, CustomerUpdateApi, QuestionCreateApi, QuestionListApi, QuestionUpdateApi, QuestionnaireCreateApi, QuestionnaireListApi, QuestionnaireUpdateApi, ResponseCreateApi, ResponseListApi, ResponseUpdateApi, UserCreateApi, UserListApi, UserUpdateApi

urlpatterns = [
    path('user/api/create',UserCreateApi.as_view()),
    path('user/api',UserListApi.as_view()),
    path('user/api/<int:pk>',UserUpdateApi.as_view()),
    path('question/api/create',QuestionCreateApi.as_view()),
    path('question/api',QuestionListApi.as_view()),
    path('question/api/<int:pk>',QuestionUpdateApi.as_view()),
    path('response/api/create',ResponseCreateApi.as_view()),
    path('response/api',ResponseListApi.as_view()),
    path('response/api/<int:pk>',ResponseUpdateApi.as_view()),
    path('questionnqire/api/create',QuestionnaireCreateApi.as_view()),
    path('questionnqire/api',QuestionnaireListApi.as_view()),
    path('questionnqire/api/<int:pk>',QuestionnaireUpdateApi.as_view()),
    path('client/api/create',CustomerCreateApi.as_view()),
    path('client/api',CustomerListApi.as_view()),
    path('client/api/<int:pk>',CustomerUpdateApi.as_view()),
]