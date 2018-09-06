from django.shortcuts import render
from .models import Customer, Profession
from .serializers import CustomerSerializer, ProfessionSerializer
from rest_framework import viewsets


# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer



