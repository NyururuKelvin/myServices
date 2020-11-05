from django.urls import path
from classViews.views import service

urlpatterns = [
    path('', service.get_services),
    path('add', service.add_service),
    path('delete/<int:service_id>', service.delete_service),
    path('update/<int:service_id>', service.update_service)
]

