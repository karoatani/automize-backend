from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Account(AbstractUser):
    """ Custom user model """
    pass


class Person(models.Model):
    
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20, default='')
     
class Debt(models.Model):
    DEBT_TYPE = (
            ("CR", "Creditor"),
           ("DR", "Debtor"),
    )
    PAYMENT_FREQUENCY = (
            ("MONTHLY", "Monthly"),
           ("BI-MONTHLY", "Bi-Monthly"),
           ("WEEKLY", "Weekly"),
           ("BI-WEEKLyY", "Bi-Weekly"),
           ("QUARTERLY", "Quarterly"),
           ("SEMI-ANNUALLY", "Semi-Annually"),
           ("ANNUALLY", "Annually"),
    )
    PAYMENT_METHOD = (
            ("BANK TRANSFER", "Bank Transfer"),
           ("CASH", "Cash"),
           ("CREDIT CARD", "Credit Card"),
           ("DEBIT CARD", "Debit Card"),
           ("CHECK", "Check"),
           ("OTHERS", "Others"),
           )
    user = models.ForeignKey("Account", on_delete=models.CASCADE, default='')
    type = models.CharField(max_length=255, choices=DEBT_TYPE)
    person = models.ForeignKey("Person", on_delete=models.CASCADE, related_name="debt")
    amount = models.FloatField()
    currency = models.CharField(max_length=4)
    due_date = models.DateTimeField()
    interest_rate = models.FloatField(default=0)
    
    date_created = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    payment_frequency = models.CharField(max_length=20, choices=PAYMENT_FREQUENCY) 
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD)
    is_paid = models.BooleanField(default=False)
    is_bad_debt = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
