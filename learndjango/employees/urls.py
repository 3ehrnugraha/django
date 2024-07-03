from django.urls import path
from . import views
from . import api_views

urlpatterns = [
    path('employees/', views.employees, name='employees'),
    path('employees/details/<int:pk>/', views.EmployeeDetailView.as_view(), name='details'),
    path('add_employee/', views.add_employee, name='add_employee'),

    path('api/employee/', api_views.employee_list),
    path('api/employee/add/', api_views.employee_add),
    path('api/employee/<int:pk>/', api_views.employee_detail),
]