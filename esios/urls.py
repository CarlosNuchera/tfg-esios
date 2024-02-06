from rest_framework import routers
from .api import EsiosViewSet

router = routers.DefaultRouter()

router.register('api/esios', EsiosViewSet, 'esios')
urlpatterns = router.urls