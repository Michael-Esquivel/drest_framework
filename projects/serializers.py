'''
Herramienta que convierte datos complejos, como objetos Python, en datos más simples y universales, 
como JSON, que pueden ser fácilmente almacenados.
'''

from rest_framework import serializers
from .models import Project

class Serializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__' #Ademas de que guarda todos, permite ver el ID de cada registro
        read_only_fields = ('created_at', )