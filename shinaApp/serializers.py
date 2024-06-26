from rest_framework import serializers
from .models import Basket, User, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BasketSerializer(serializers.ModelSerializer):
    products = ProductSerializer(many=True, read_only=True) 
       
    class Meta:
        model = Basket
        fields = ['user', 'products']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
