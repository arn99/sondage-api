from django.db import models
from django.contrib.auth.models import (
     AbstractBaseUser
)


class User(AbstractBaseUser):
    username = models.CharField(
        verbose_name='username address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    commercial = models.BooleanField(default=True) # a superuser
    code_commercial = models.CharField(max_length = 100, unique=True,)
    date_created = models.DateField(auto_created=True)

    # notice the absence of a "Password field", that is built in.

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['username', 'password'] # username & Password are required by default.

    def get_full_name(self):
        # The user is identified by their username address
        return self.username

    def get_short_name(self):
        # The user is identified by their username address
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin




class Inquiry(models.Model):
    title = models.CharField(max_length = 100, default="")
    is_completed = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True)
    creator = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "Createur")
    def __str___(self):
        return self.title
class Customer(models.Model):
    fullname = models.CharField(max_length = 250)
    sexe = models.CharField(max_length = 250)
    age = models.CharField(max_length = 250)
    commercial = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        
    )
    def __str___(self):
        return self.fullname


class Question(models.Model):
    body = models.CharField(max_length = 250)
    date_created = models.DateField(auto_created=True)
    inquiry = models.ForeignKey(Inquiry, on_delete = models.CASCADE, related_name = "Enquete")
    recommendation = models.CharField(max_length = 250)
    def __str___(self):
        return self.body
class Response(models.Model):
    body = models.CharField(max_length = 250)
    is_valid = models.BooleanField(default=False)
    date_created = models.DateField(auto_created=True)
    question = models.ForeignKey(Question, on_delete = models.CASCADE)
    def __str___(self):
        return self.body

class Questionnaire(models.Model):
    date_created = models.DateField(auto_created=True)
    questions = models.ForeignKey(Question, on_delete = models.CASCADE)
    responses = models.ForeignKey(Response, on_delete = models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE, related_name = "client")
    def __str___(self):
        return self.customer

