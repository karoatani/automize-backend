import csv
from typing import Any
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Account
from .serializers import UserAccountRegisterSeralizer
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import Debt, Person
from .serializers import UserAddDebtSerializer, UserDebtListSerializer, UserDebtUpdateSerializer, UserDebtDeleteSerializer, UserDebtRetrieveSerializer

class UserAccountLoginAPiView(TokenObtainPairView):
    
    def post(self, request: Request, *args, **kwargs) -> Response:

        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        user_id = AccessToken(serializer.validated_data["access"])["user_id"]
        custom_response = {
            "id" : user_id,
            "refresh": serializer.validated_data.get("refresh"),
            "access" : serializer.validated_data.get("access")
        }
        return Response(custom_response, status=status.HTTP_200_OK)


class UserAccountRefreshAPiView(TokenRefreshView):
    pass

class UserAccountRegisterAPiView(generics.CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = UserAccountRegisterSeralizer


    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        validated_data = serializer.validated_data 
        validated_data.update({
            "password": make_password(validated_data["password"])
        })
        instance = serializer.save()
        
        headers = self.get_success_headers(serializer.data)
        custom_response = {
            "id": instance.id,
            "first_name": instance.first_name,
            "last_name": instance.last_name,
            "username": instance.username,
            "email": instance.email,
            "password": instance.password
        }
        return Response(custom_response, status=status.HTTP_201_CREATED, headers=headers)


class UserAddDebtAPIView(generics.CreateAPIView):
    queryset = Debt.objects.all()
    serializer_class = UserAddDebtSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        user_id = self.request.user.id
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.data

        person = data.pop("person")
        
        user = Account.objects.get(id=user_id)
        person = Person.objects.create(**person)
        
        debt = Debt.objects.create(user=user, person=person, **data)
        return Response(serializer.data)


class UserDebtListAPIView(generics.ListAPIView):
    queryset = Debt.objects.all()
    serializer_class = UserDebtListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.kwargs["pk"]
        return super().get_queryset().filter(user__id=user_id, is_deleted=False)
    


class UserDebtUpdateAPIView(generics.UpdateAPIView):
    queryset = Debt.objects.all()
    serializer_class = UserDebtUpdateSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user_id = self.request.user.id
        return super().get_queryset().filter(user__id=user_id, is_deleted=False)
    
    def put(self, request, *args, **kwargs):
        debt_id = self.kwargs["pk"]
        
        partial = kwargs.pop('partial', False)
        instance = self.get_object()

        serializer = self.get_serializer(data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.data
        person = data.pop("person")
        
        Debt.objects.filter(id=debt_id).update(**data)
        Person.objects.filter(debt__id=debt_id).update(**person)
        
        if getattr(instance, '_prefetched_objects_cache', None):
            instance._prefetched_objects_cache = {}

        return Response(serializer.data)
    

class UserDebtDeleteAPIView(generics.UpdateAPIView):
    queryset = Debt.objects.all()
    serializer_class = UserDebtDeleteSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user_id = self.request.user.id
        return super().get_queryset().filter(user__id=user_id)
    

class UserDebtRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Debt.objects.all()
    serializer_class = UserDebtRetrieveSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
        return super().get_queryset().filter(user__id=user_id, is_deleted=False)
    
    