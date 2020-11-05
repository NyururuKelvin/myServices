from django.urls import path, include
from classViews import views

urlpatterns = [
    path('service/', include('classViews.routes.service')),
    path('service_type/', include('classViews.routes.serviceType')),
    path('company/', include('classViews.routes.company')),
    path('company_service/', include('classViews.routes.companyService')),
    path('working_hour/', include('classViews.routes.workingHour')),
    path('service_booking/', include('classViews.routes.serviceBooking')),
]
