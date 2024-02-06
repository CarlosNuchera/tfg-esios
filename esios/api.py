from .models import Esios
from rest_framework import viewsets, permissions
from .serializers import EsisosSeriealizers

class EsiosViewSet(viewsets.ModelViewSet):
    queryset = Esios.objects.all()
    permission_classes = [permissions.AllowAny] #cambiar a futuro para usuarios autenticados
    serializer_class = EsisosSeriealizers