from django.shortcuts import render
from api.models import car_list
from api.serializers import UserSerializer
from rest_framework import viewsets

class UserViewSet(viewsets.ModelViewSet):
    queryset = car_list.objects.all()
    serializer_class = UserSerializer

# Create your views here.
