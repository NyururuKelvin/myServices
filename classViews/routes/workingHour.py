from django.urls import path
from classViews.views import workingHour

urlpatterns = [
    path('', workingHour.get_working_hours),
    path('add', workingHour.add_working_hour),
    path('delete/<int:working_hour_id>', workingHour.delete_working_hour),
    path('update/<int:working_hour_id>', workingHour.update_working_hour)
]

