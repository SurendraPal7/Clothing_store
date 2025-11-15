from django.urls import path
from . import views_admin

urlpatterns = [
    path('', views_admin.sales_dashboard, name='sales_dashboard'),
]
