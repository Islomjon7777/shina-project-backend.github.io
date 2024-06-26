from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Basket, Product
from .serializers import *
from django.contrib.auth import get_user_model

User = get_user_model()

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        user = self.request.user
        basket, created = Basket.objects.get_or_create(user=user)
        product = serializer.save()
        basket.products.add(product)
        basket.save()

class BasketViewSet(viewsets.ModelViewSet):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Basket.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
