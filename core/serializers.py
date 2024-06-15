from rest_framework import serializers
from .models import Account, Debt, Person


class UserAccountRegisterSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["first_name", "last_name","username","email", "password"]



class UserAccountSeralizer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ["id","first_name", "last_name", "username", "email"]


class UserAddDebtPersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ["first_name", "last_name", "phone_number"]

class UserAddDebtSerializer(serializers.ModelSerializer):
    person = UserAddDebtPersonSerializer()
    class Meta: 
        model = Debt
        fields = ["person","type", "amount", "currency", "due_date", "interest_rate", "payment_frequency", "payment_method"]


class UserDebtListSerializer(serializers.ModelSerializer):
    person = UserAddDebtPersonSerializer() 
    user = UserAccountSeralizer()
    class Meta:
        model = Debt
        fields = ["id","user","person","type", "amount", "currency", "due_date", "interest_rate", "status","payment_frequency", "payment_method"]




class UserDebtUpdateSerializer(serializers.ModelSerializer):
    person = UserAddDebtPersonSerializer() 
    class Meta:
        model = Debt
        fields = ["person","type", "amount", "currency", "due_date", "interest_rate", "payment_frequency", "payment_method", "status"]



class UserDebtDeleteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Debt
        fields = ["is_deleted"]



class UserDebtRetrieveSerializer(serializers.ModelSerializer):
    person = UserAddDebtPersonSerializer() 
    user = UserAccountSeralizer()
    class Meta:
        model = Debt
        fields = ["id","user","person","type", "amount", "currency", "due_date", "interest_rate", "status","payment_frequency", "payment_method"]


class UserDebtDashboardSerializer(serializers.ModelSerializer):
    person = UserAddDebtPersonSerializer()
    how_long = serializers.SerializerMethodField()
    class Meta:
        model = Debt
        fields = ["id", "person", "amount", "due_date", "status","how_long"]

    def get_how_long(self,obj):
        return obj.how_long