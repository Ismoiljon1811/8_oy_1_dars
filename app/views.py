from django.shortcuts import render
from .serializers import CarSerializer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from .models import Car


class CarAPIView(ListAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarAPIDetail(RetrieveAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer