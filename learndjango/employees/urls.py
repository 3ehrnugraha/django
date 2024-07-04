from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .api_views import EmployeeViewSet

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet)

urlpatterns = [
    # path('employees/', views.employees, name='employees'),
    # path('employees/details/<int:pk>/', views.EmployeeDetailView.as_view(), name='details'),
    # path('add_employee/', views.add_employee, name='add_employee'),
    path('', include(router.urls)),
]