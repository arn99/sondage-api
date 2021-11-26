from django.db import models
from django.contrib.auth.models import (
     AbstractUser
)
from django.utils import timezone
from django.dispatch import receiver
from .managers import UserManager

OTHER_CHOICES = (
    (1, "Choix"),
    (2, "Autre")
)

class CustomUser(AbstractUser):
    is_commercial = models.BooleanField(default=False)
    code_commercial = models.CharField(unique=True, max_length=200)

    
    

class Inquiry(models.Model):
    title = models.CharField(max_length = 100, default="")
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True)
    creator = models.ForeignKey(CustomUser, on_delete = models.CASCADE, related_name = "Createur")
    def __str__(self):
        return self.title
class Customer(models.Model):
    fullname = models.CharField(max_length = 250)
    sexe = models.CharField(max_length = 250)
    age = models.CharField(max_length = 250)
    commercial = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        
    )
    def __str__(self):
        return self.fullname


class Question(models.Model):
    body = models.CharField(max_length = 250)
    date_created = models.DateField(auto_created=True)
    inquiry = models.ForeignKey(Inquiry, on_delete = models.CASCADE)
    recommendation = models.CharField(max_length = 250)
    
    def __str__(self):
        return self.body
class Response(models.Model):
    choice = models.CharField(max_length = 250)
    type = models.IntegerField( choices=OTHER_CHOICES, default=1)
    is_valid = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    def __str__(self):
        return self.choice

class Questionnaire(models.Model):
    date_created = models.DateField(auto_created=True,default=timezone.now)
    questions = models.ForeignKey(Question, on_delete = models.CASCADE)
    responses = models.ForeignKey(Response, on_delete = models.CASCADE)
    other = models.CharField(max_length = 250, default='none')
    code_commercial = models.CharField( max_length=200)
    customer = models.CharField( max_length=200)
    def __str__(self):
        return self.customer

