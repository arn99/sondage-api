from rest_framework import  serializers
from .models import Customer, Inquiry, Question, Questionnaire, Response, CustomUser
from rest_flex_fields import FlexFieldsModelSerializer
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = '__all__'

# Register serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','username','password')
        extra_kwargs = {
            'password':{'write_only': True},
        }
    def create(self, validated_data):
        user = CustomUser.objects.create_user(validated_data['username'],password = validated_data['password'] ,email=validated_data['email'])
        return user


class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__'


class ResponseSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Response
        fields = ['id', 'choice']
class QuestionSerializer(FlexFieldsModelSerializer):
    response = ResponseSerializer(source='response_set', many=True)
    class Meta:
        model = Question
        fields = ['id', 'body', 'response']
        expandable_fields = {
          'response': (ResponseSerializer, {'many': True})
        }
class InquirySerializer(FlexFieldsModelSerializer):
    question = QuestionSerializer(source='question_set', many=True)
    class Meta:
        model = Inquiry
        fields = ['id', 'title', 'question']
        expandable_fields = {
          'question': (QuestionSerializer, {'many': True})
        }

class QuestionnaireSerializer(serializers.ModelSerializer):
     class Meta:
        model = Questionnaire
        fields = ['id', 'customer', 'questions', 'responses']