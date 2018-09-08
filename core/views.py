from django.shortcuts import render
from .models import Customer, Profession, Document, DataSheet
from .serializers import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response


# Create your views here.


class CustomerViewSet(viewsets.ModelViewSet):

    serializer_class = CustomerSerializer

    def get_queryset(self):
        print("get_queryset_func")
        # how to set breakpoints
        # import pdb; pdb.set_trace()
        params = self.request.query_params

        if 'name' in params:
            customers = Customer.objects.filter(name=params['name'])
        else:
            customers = Customer.objects.all()
        # active_customers = Customer.objects.all()
            #.filter(active=True)

        return customers

    def list(self, request, *args, **kwargs):
        print("list_func")
        customers = self.get_queryset()
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    @action(detail=True)
    def deactivate(self, request, **kwargs):
        customer = self.get_object()
        customer.active = False
        customer.save()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)

    @action(detail=False)
    def deactivate_all(self, request, **kwargs):
        customers = Customer.objects.all()
        customers.update(active=False)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def activate_all(self, request, **kwargs):
        customers = Customer.objects.all()
        customers.update(active=True)
        serializer = CustomerSerializer(customers, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['POST'])
    def set_status(self, request, **kwargs):

        customer = self.get_object()

        if 'active' in request.data:
            customer.active = request.data['active']
        else:
            print("wrong key")

        customer.save()
        serializer = CustomerSerializer(customer)
        return Response(serializer.data)



    # @action(detail=True)
    # def activate(self, request, **kwargs):
    #     import pdb; pdb.set_trace()
    #     customer = self.get_object()
    #     customer.active = True
    #     customer.save()
    #     serializer = CustomerSerializer(customer)
    #     return Response(serializer.data)


class ProfessionViewSet(viewsets.ModelViewSet):
    queryset = Profession.objects.all()
    serializer_class = ProfessionSerializer


class DocumentsViewSet(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentSerializer


class DataSheetsViewSet(viewsets.ModelViewSet):
    queryset = DataSheet.objects.all()
    serializer_class = DataSheetSerializer


