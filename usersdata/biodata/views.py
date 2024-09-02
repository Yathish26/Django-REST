from django.shortcuts import render
from .models import Biodata
from .serializers import BiodataSerializer
from rest_framework import generics

class Bio(generics.ListCreateAPIView):
    queryset = Biodata.objects.all()
    serializer_class = BiodataSerializer
