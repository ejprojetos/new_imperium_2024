from rest_framework.viewsets import ModelViewSet
from .models import Home, Fluxo, Feature, Depoimento, Contato
from .serializers import HomeSerializer, FluxoSerializer, ContatoSerializer, DepoimentoSerializer, FeatureSerializer

class HomeViewSet(ModelViewSet):
    queryset = Home.objects.all()
    serializer_class = HomeSerializer


class FluxoViewSet(ModelViewSet):
    queryset = Fluxo.objects.all()
    serializer_class = FluxoSerializer


class FeatureViewSet(ModelViewSet):
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer


class DepoimentoViewSet(ModelViewSet):
    queryset = Depoimento.objects.all()
    serializer_class = DepoimentoSerializer


class ContatoViewSet(ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
