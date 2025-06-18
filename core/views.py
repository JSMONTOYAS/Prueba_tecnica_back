from rest_framework import viewsets
from .models import Aspirante
from .serializers import AspiranteSerializer

class AspiranteViewSet(viewsets.ModelViewSet):
    queryset = Aspirante.objects.all()
    serializer_class = AspiranteSerializer

