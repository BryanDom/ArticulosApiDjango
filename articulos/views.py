from django.shortcuts import render
from rest_framework import generics
from articulos import serializers
from articulos.models import Articulo

class ArticulosAPIView(generics.ListCreateAPIView):
    #de forma descendente se ordena los objetos del articulo
    queryset = Articulo.objects.all().order_by('-id')
    serializer_class = serializers.ArticuloSerializer

# en este metodo 
class ArticuloAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Articulo.objects.all()
    serializer_class = serializers.ArticuloSerializer
