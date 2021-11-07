
from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from .models import Customer, Inquiry, Question, Questionnaire, Response, User
from .serializer import CustomerSerializer, InquirySerializer, QuestionSerializer, QuestionnaireSerializer, ResponseSerializer, UserSerializer

# Create your views here.
# user
class UserCreateApi(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserListApi(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserUpdateApi(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Inquiry
class InquiryCreateApi(CreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

class InquiryListApi(ListAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

class InquiryUpdateApi(RetrieveUpdateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer

# Customer
class CustomerCreateApi(CreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerListApi(ListAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

class CustomerUpdateApi(RetrieveUpdateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# Question
class QuestionCreateApi(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionListApi(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

class QuestionUpdateApi(RetrieveUpdateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

# Response
class ResponseCreateApi(CreateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

class ResponseListApi(ListAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

class ResponseUpdateApi(RetrieveUpdateAPIView):
    queryset = Response.objects.all()
    serializer_class = ResponseSerializer

# Questionnaire
class QuestionnaireCreateApi(CreateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

class QuestionnaireListApi(ListAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

class QuestionnaireUpdateApi(RetrieveUpdateAPIView):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer