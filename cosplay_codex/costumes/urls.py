from rest_framework import routers

from .views import CostumeViewSet


costume_router = routers.DefaultRouter()
costume_router.register(prefix='costume', viewset=CostumeViewSet)
