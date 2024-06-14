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
    



    