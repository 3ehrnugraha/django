from rest_framework import viewsets, filters
from .models import Division
from rest_framework.pagination import PageNumberPagination
from employees.models import Employee
from .serializers import DivisionSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100

    def paginate_queryset(self, queryset, request, view=None):
        if not queryset.ordered:
            queryset = queryset.order_by('name')  # Add a default ordering if not already ordered
        return super().paginate_queryset(queryset, request, view)

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        queryset = Division.objects.all()
        name = self.request.query_params.get('name', None)
        description = self.request.query_params.get('description', None)

        if name:
            queryset = queryset.filter(name__icontains=name)
        if description:
            queryset = queryset.filter(description__icontains=description)

        return queryset
