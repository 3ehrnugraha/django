from rest_framework import serializers
from .models import Project, Task
from employees.models import Employee


class ProjectSerializer(serializers.ModelSerializer):
    employee_ids = serializers.PrimaryKeyRelatedField(queryset=Employee.objects.all(), many=True, write_only=True)

    class Meta:
        model = Project
        fields = ['id', 'name', 'description', 'employees', 'employee_ids']
        read_only_fields = ['employees']

    def create(self, validated_data):
        employee_ids = validated_data.pop('employee_ids')
        project = Project.objects.create(**validated_data)
        project.employees.set(employee_ids) 
        return project

    def update(self, instance, validated_data):
        employee_ids = validated_data.pop('employee_ids')
        instance.name = validated_data.get('name', instance.name)
        instance.description = validated_data.get('description', instance.description)
        instance.save()
        instance.employees.set(employee_ids)
        return instance
    
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'start_date', 'due_date', 'status', 'priority', 'created_at', 'updated_at', 'employee', 'project']
        