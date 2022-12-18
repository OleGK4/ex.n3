from django.urls import path, include
from rest_framework import routers
from .views import ProductViewSet, UserViewSet


router = routers.DefaultRouter()
router.register(r'product', ProductViewSet)
router.register(r'user', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_framework.urls', namespace='rest_framework'))
]
