
from rest_framework import routers, serializers, viewsets
from api.models import car_list


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = car_list
        fields = ['nome', 'marca', 'placa', 'cor']