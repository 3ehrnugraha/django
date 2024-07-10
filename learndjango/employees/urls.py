from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import api_views
from .api_views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    # path('employees/', views.employees, name='employees'),
    # path('employees/details/<int:pk>/', views.EmployeeDetailView.as_view(), name='details'),
    # path('add_employee/', views.add_employee, name='add_employee'),
    path('', include(router.urls)),
    path('employee_distribution_by_division/', api_views.employee_distribution_by_division, name='employee_distribution_by_division'),
    path('salary_distribution/', api_views.salary_distribution, name='salary_distribution'),
]