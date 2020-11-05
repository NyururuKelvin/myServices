from django.urls import path
from classViews.views import company

urlpatterns = [
    path('', company.get_companies),
    path('add', company.add_company),
    path('delete/<int:company_id>', company.delete_company),
    path('update/<int:company_id>', company.update_company)
]

