from django.shortcuts import render
from .models import Product
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import ProductSerializer, UserSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
