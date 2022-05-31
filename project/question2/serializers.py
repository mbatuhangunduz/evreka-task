from rest_framework import serializers
from .models import *


class OperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operation
        fields = '__all__'
        depth = 1


class BinSerializer(serializers.ModelSerializer):

    class Meta:
        model = Bin
        fields = '__all__'


class BinOperationListSerializer(serializers.ModelSerializer):
    operation = serializers.SerializerMethodField(read_only=True)
    bin = BinSerializer(read_only=True)

    def get_operation(self, obj):
        return obj.operation.name
        
    class Meta:
        model = BinOperation
        fields = '__all__'
        depth = 1


class BinOperationSerializer(serializers.ModelSerializer):

    class Meta:
        model = BinOperation
        fields = '__all__'