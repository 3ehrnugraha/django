from django.urls import path
from . import views

urlpatterns = [
    path('employees/', views.employees, name='employees'),
    path('employees/details/<int:pk>/', views.EmployeeDetailView.as_view(), name='details'),
    path('add_employee/', views.add_employee, name='add_employee'),
]