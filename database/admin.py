from django.contrib import admin
from database import models
# Register your models here.
admin.site.register(models.ServiceType)
admin.site.register(models.Service)
admin.site.register(models.Company)
admin.site.register(models.CompanyService)
admin.site.register(models.ServiceBooking)
admin.site.register(models.WorkingHour)