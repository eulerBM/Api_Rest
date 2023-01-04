
from rest_framework import routers, serializers, viewsets
from api.models import lista_de_carros


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = lista_de_carros
        fields = ['nome', 'marca', 'placa', 'cor']