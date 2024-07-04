from rest_framework import viewsets
from .models import Division
from .serializers import DivisionSerializer

class DivisionViewSet(viewsets.ModelViewSet):
    queryset = Division.objects.all()
    serializer_class = DivisionSerializer