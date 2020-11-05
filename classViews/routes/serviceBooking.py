from django.urls import path
from classViews.views import serviceBooking

urlpatterns = [
    path('', serviceBooking.get_service_booking),
    path('add', serviceBooking.add_service_booking),
    path('delete/<int:service_booking_id>', serviceBooking.delete_service_booking),
    path('update/<int:service_booking_id>', serviceBooking.update_service_booking)
]

