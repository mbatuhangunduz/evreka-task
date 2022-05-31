from .models import *
from rest_framework import serializers
import re


class VehicleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Vehicle
        fields = '__all__'


class NavigationRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = NavigationRecord
        fields = '__all__'


class NavigationRecordListSerializer(serializers.ModelSerializer):
    vehicle_plate = serializers.SerializerMethodField()

    def get_vehicle_plate(self, obj):
        plate = obj.vehicle.plate
        """ This method is used to separate the numbers and letters on the plate in order to get a response like the e.g. data."""
        plate = re.split('(\d+)',plate)
        return plate[0] + plate[1] + ' ' + plate[2] + ' ' + plate[3]
    class Meta:
        model = NavigationRecord
        fields = ["latitude", "longitude", "vehicle_plate", "datetime"]

    

