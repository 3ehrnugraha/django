from rest_framework import viewsets, filters
from .models import Division
from employees.models import Employee
from .serializers import DivisionSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer

    def get_queryset(self):
        queryset = Division.objects.all()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if description:
            queryset = queryset.filter(description__icontains=description)

        return queryset
