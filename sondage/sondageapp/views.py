
from django.shortcuts import render
from rest_framework import generics
from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Customer, Inquiry, Question, Questionnaire, Response, CustomUser
from .serializer import CustomerSerializer, InquirySerializer, QuestionSerializer, QuestionnaireSerializer, RegisterSerializer, ResponseSerializer, CustomUserSerializer

# Create your views here.
# user
class CustomUserCreateApi(CreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": CustomUserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "CustomUser Created Successfully.  Now perform Login to get your token",
        })

class CustomUserListApi(ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserUpdateApi(RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

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

class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)