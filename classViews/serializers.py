from django.contrib.auth.models import User
from rest_framework import serializers
from database import models
from datetime import datetime


class ServiceTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ServiceType
        fields = ('id', 'name',)

    def create(self, validated_data):
        return models.ServiceType.objects.create(**validated_data)


class ServiceSerializer(serializers.ModelSerializer):
    serviceType = ServiceTypeSerializer(many=False)

    class Meta:
        model = models.Service
        fields = ('id', 'name', 'serviceType', 'description',)
        read_only_fields = ('CREATED_AT', 'UPDATED_AT')

    # def create(self, validated_data):
    #     serviceType = validated_data.pop('serviceType')
    #     serviceType = models.ServiceType.objects.get_or_404(pk=serviceType)[0]
    #     return models.Service.objects.create(serviceType=serviceType, **validated_data)


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = ('id', 'name', 'email', 'description',)


class WorkingHourSerializer(serializers.ModelSerializer):
    # _from = serializers.TimeField()
    # _to = serializers.TimeField()
    # day = serializers.IntegerField()
    company = CompanySerializer()

    # lunch_start = serializers.TimeField(allow_null=True)
    # lunch_end = serializers.TimeField(allow_null=True)

    class Meta:
        model = models.WorkingHour
        fields = ('id', '_from', '_to', 'day', 'company', 'lunch_start', 'lunch_end',)


class CompanyServiceSerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    company = CompanySerializer()

    class Meta:
        model = models.CompanyService
        fields = ['id', 'service', 'description', 'company', 'price']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email',)


class ServiceBookingSerializer(serializers.ModelSerializer):
    service = CompanyServiceSerializer()
    user = UserSerializer()

    class Meta:
        model = models.ServiceBooking
        fields = ('id','user', 'service', 'status',)

# class ServiceSerializer(serializers.ModelSerializer):
#     name =serializers.CharField()
#     serviceType = ServiceTypeSerializer()
#     description = serializers.CharField(max_length=5000)
#     CREATED_AT = serializers.DateTimeField(allow_null=True)
#     UPDATED_AT = serializers.DateTimeField(allow_null=True)
#     class Meta:
#         model = models.Service
