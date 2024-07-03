from .serializers import EmployeeSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer

@api_view(['GET'])
def employee_list(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def employee_add(request):
    serializer = EmployeeSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        response_data = {
            'message': 'Employee created successfully!',
            'data': serializer.data,
        }
        return Response(response_data, status=201)
    return Response(serializer.errors, status=400)

@api_view(['GET', 'PUT', 'DELETE'])
def employee_detail(request, pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except Employee.DoesNotExist:
        return Response({'Error': 'Employee not found'}, status=404)

    if request.method == 'GET':
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Employee updated successfully!',
                'data': serializer.data,
            }
            return Response(response_data)
        return Response(serializer.errors, status=400)
    
    elif request.method == 'DELETE':
        employee.delete()
        # Customize the response for a successful deletion
        return Response({'message': 'Food item deleted successfully!'}, status=204)