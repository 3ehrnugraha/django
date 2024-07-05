from rest_framework import serializers
from employees.serializers import EmployeeSerializer
from .models import Division

class DivisionSerializer(serializers.ModelSerializer):
    employees = EmployeeSerializer(many=True, read_only=True)
    class Meta:
        model = Division
        fields = '__all__'