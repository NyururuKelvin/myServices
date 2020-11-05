
from django.urls import path
from classViews.views import serviceType

urlpatterns = [
    path('', serviceType.get_service_types),
    path('add', serviceType.add_service_type),
    path('delete/<int:service_id>', serviceType.delete_service_type),
    path('update/<int:service_id>', serviceType.update_service_type)
]