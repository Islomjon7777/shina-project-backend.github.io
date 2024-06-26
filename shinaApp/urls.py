from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BasketViewSet, ProductViewSet, UserViewSet
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()
router.register(r'baskets', BasketViewSet)
router.register(r'products', ProductViewSet)
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
