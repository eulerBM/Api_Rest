from django.shortcuts import render
from api.models import lista_de_carros
from api.serializers import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = lista_de_carros.objects.all()
    serializer_class = UserSerializer

# Create your views here.
