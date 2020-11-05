from django.urls import path
from classViews.views import companyService

urlpatterns = [
    path('', companyService.get_company_services),
    path('add', companyService.add_company_service),
    path('delete/<int:company_service_id>', companyService.delete_company_service),
    path('update/<int:company_service_id>', companyService.update_company_service)
]

