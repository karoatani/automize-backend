from rest_framework import serializers
from .models import Account


class UserAccountRegisterSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["first_name", "last_name","username","email", "password"]



class UserAccountSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id","first_name", "last_name", "username", "email"]