from rest_framework import serializers
from .models import *


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('id', 'name', 'address', 'professions', 'data_sheet', 'active')


class ProfessionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profession
        fields = ('id', 'title', 'description', 'detailed_description')


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Document
        fields = ('id', 'doc_type', 'customer')


class DataSheetSerializer(serializers.ModelSerializer):

    class Meta:
        model = DataSheet
        fields = ('id', 'description', 'historical_data')
