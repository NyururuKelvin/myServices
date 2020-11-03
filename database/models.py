from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Service(models.Model):
    name = models.CharField(max_length=100)
    serviceType = models.ForeignKey("ServiceType", on_delete=models.SET_NULL, null=True, related_name='services')
    description = models.TextField()
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)


class ServiceType(models.Model):
    name = models.CharField(max_length=100)
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)


class Company(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    description = models.TextField()
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)


class WorkingHour(models.Model):
    _from = models.TimeField()
    _to = models.TimeField()
    day = models.IntegerField()
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name='working_hours')
    lunch_start = models.TimeField(null=True)
    lunch_end = models.TimeField(null=True)


class CompanyService(models.Model):
    service = models.ForeignKey(Service, on_delete=models.SET_NULL, related_name="company_services", null=True)
    description = models.TextField()
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, related_name="my_services")
    price = models.IntegerField()
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)


class ServiceBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,null=True, related_name="bookings")
    service = models.ForeignKey(CompanyService, on_delete=models.SET_NULL, null=True, related_name='bookings')
    status = models.IntegerField()
    CREATED_AT = models.DateTimeField(auto_now_add=True)
    UPDATED_AT = models.DateTimeField(auto_now=True)
