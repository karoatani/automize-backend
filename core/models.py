from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    """ Custom user model """
    pass




class Statement(models.Model):
    user_statement = models.JSONField()
    user = models.ForeignKey("Account", on_delete=models.CASCADE)