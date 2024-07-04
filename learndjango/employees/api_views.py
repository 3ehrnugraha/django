from .serializers import EmployeeSerializer
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Employee, Division
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    @permission_classes([IsAuthenticated])
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data = {
                'message': 'Employee created successfully!',
                'data': serializer.data,
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        # Check if 'division' is provided in request data
        if 'division' in request.data:
            division_id = request.data['division']
            instance.division_id = division_id  # Update the division ID
            instance.save()
        serializer.save()
        response_data = {
            'message': 'Employee updated successfully!',
            'data': serializer.data,
        }
        return Response(response_data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({'message': 'Employee deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def employee_list(request):
#     employees = Employee.objects.all()
#     serializer = EmployeeSerializer(employees, many=True)
#     return Response(serializer.data)

# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def employee_add(request):
#     serializer = EmployeeSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         response_data = {
#             'message': 'Employee created successfully!',
#             'data': serializer.data,
#         }
#         return Response(response_data, status=201)
#     return Response(serializer.errors, status=400)

# @api_view(['GET', 'PUT', 'DELETE'])
# def employee_detail(request, pk):
#     try:
#         employee = Employee.objects.get(pk=pk)
#     except Employee.DoesNotExist:
#         return Response({'Error': 'Employee not found'}, status=404)

#     if request.method == 'GET':
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             response_data = {
#                 'message': 'Employee updated successfully!',
#                 'data': serializer.data,
#             }
#             return Response(response_data)
#         return Response(serializer.errors, status=400)
    
#     elif request.method == 'DELETE':
#         employee.delete()
#         # Customize the response for a successful deletion
#         return Response({'message': 'Food item deleted successfully!'}, status=204)