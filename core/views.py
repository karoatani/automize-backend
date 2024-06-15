import datetime
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
from .serializers import UserAddDebtSerializer, UserDebtListSerializer, UserDebtUpdateSerializer, UserDebtDeleteSerializer, UserDebtRetrieveSerializer, UserDebtDashboardSerializer

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
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDebtListAPIView(generics.ListAPIView):
    queryset = Debt.objects.all()
    serializer_class = UserDebtListSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user_id = self.request.user.id
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
    
    

# class test(generics.ListAPIView):
#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)
from django.db.models.functions import ExtractDay, Coalesce
from django.db.models import Sum, Avg, Max, Min, Value
from django.utils import timezone
class UserDebtDashboardAPIView(APIView):
    query_set = Debt.objects.all()
    permission_classes = [IsAuthenticated]
    


    def get(self, request, *args, **kwargs):
        user_id = self.request.user.id
        query_set = self.query_set.filter(user__id=user_id, is_deleted=False)
        query_set_by_cr =query_set.filter(type="CR")
        query_set_by_dr =query_set.filter(type="DR")
        
        total_debt_owed_by_user = query_set_by_cr.count()
        total_amount_debt_owed_by_user = query_set_by_cr.aggregate(amount_sum=Coalesce(Sum("amount"), Value(0.0)))["amount_sum"]
        
        total_debt_to_user = query_set_by_dr.count()
        total_amount_debt_to_user = query_set_by_dr.aggregate(amount_sum=Coalesce(Sum("amount"), Value(0.0)))["amount_sum"]
        
        average_debt_amount_owed_by_user = query_set_by_cr.aggregate(amount_avg= Coalesce(Avg("amount"), Value(0.0)))["amount_avg"]
        average_debt_amount_to_user = query_set_by_dr.aggregate(amount_avg = Coalesce(Avg("amount"), Value(0.0)))["amount_avg"]
        
        largest_debt_amount_owed_by_user = query_set_by_cr.aggregate(amount_max= Coalesce(Max("amount"), Value(0.0)))["amount_max"]
        largest_debt_amount_to_user = query_set_by_dr.aggregate(amount_max= Coalesce(Max("amount"), Value(0.0)))["amount_max"]
        
        smallest_debt_amount_owed_by_user = query_set_by_cr.aggregate(amount_min= Coalesce(Min("amount"), Value(0.0)))["amount_min"]
        smallest_debt_amount_to_user = query_set_by_dr.aggregate(amount_min= Coalesce(Min("amount"), Value(0.0)))["amount_min"]
        
        total_amount_owed_by_user_paid = query_set.filter(status="PAID", type="CR").aggregate(total=Coalesce(Sum("amount"), Value(0.0)))["total"]
        total_amount_to_user_paid = query_set.filter(status="PAID", type="DR").aggregate(total=Coalesce(Sum("amount"), Value(0.0)))["total"]
        

        
        
        
        current_date = timezone.now()
        day = datetime.datetime.now().day
        over_due_debt_owed_by_user = query_set.filter(status="NOT PAID", type="CR").filter(due_date__lte=current_date).count()
        over_due_debt_to_user = query_set.filter(status="NOT PAID", type="DR").filter(due_date__lte=current_date).count()

        
        
        
        
        up_coming_payments = query_set.order_by("due_date").annotate(how_long=day - ExtractDay("due_date"))

        serializer = UserDebtDashboardSerializer(up_coming_payments, many=True)
        data = {
            "total_debt_owed_by_user": total_debt_owed_by_user,
            "total_amount_debt_owed_by_user": total_amount_debt_owed_by_user,
            "total_debt_to_user": total_debt_to_user,
            "total_amount_debt_to_user": total_amount_debt_to_user,
            "average_debt_amount_owed_by_user" : average_debt_amount_owed_by_user,
            "average_debt_amount_to_user": average_debt_amount_to_user,
            "largest_debt_amount_owed_by_user": largest_debt_amount_owed_by_user,
            "largest_debt_amount_to_user": largest_debt_amount_to_user,
            "smallest_debt_amount_owed_by_user" :smallest_debt_amount_owed_by_user,
            "smallest_debt_amount_to_user" : smallest_debt_amount_to_user,
            "total_amount_owed_by_user_paid": total_amount_owed_by_user_paid,
            "total_amount_to_user_paid" : total_amount_to_user_paid,
            "over_due_debt_owed_by_user": over_due_debt_owed_by_user,
            "over_due_debt_to_user" : over_due_debt_to_user,
            "up_coming_payments" : serializer.data
        }    
            
        
        return Response(data)