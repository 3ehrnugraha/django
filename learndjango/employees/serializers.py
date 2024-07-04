from rest_framework import serializers
from .models import Employee
from division.serializers import DivisionSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    division = DivisionSerializer(required=False, allow_null=True)
    class Meta:
        model = Employee
        fields = '__all__'