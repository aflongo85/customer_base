from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'name', 'address', 'professions', 'data_sheet')


class ProfessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profession
        fields = ('id', 'title', 'description')

