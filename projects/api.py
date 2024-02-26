'''
Viewsets define la lógica de las vistas que manejan las acciones CRUD para los datos del modelo.
'''
from rest_framework import viewsets, permissions
from .models import Project
from .serializers import Serializer

class Viewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = Serializer

