from rest_framework.routers import DefaultRouter
from .views import HomeViewSet, FluxoViewSet, FeatureViewSet, DepoimentoViewSet, ContatoViewSet

router = DefaultRouter()
router.register(r'home', HomeViewSet, basename='home')
router.register(r'fluxo', FluxoViewSet, basename='fluxo')
router.register(r'feature', FeatureViewSet, basename='feature')
router.register(r'depoimento', DepoimentoViewSet, basename='depoimento')
router.register(r'contato', ContatoViewSet, basename='contato')

urlpatterns = router.urls
