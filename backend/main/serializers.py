from rest_framework import serializers
from main.models import SimplifiedPackage

class SimplifiedPackageSerializer(serializers.ModelSerializer):

    class Meta:
        model = SimplifiedPackage
        fields = '__all__'


class CarSerializer(serializers.Serializer):
    vin = serializers.CharField()

class CarPositionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    vin = serializers.CharField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
    datetime = serializers.DateTimeField()