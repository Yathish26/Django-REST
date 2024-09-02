from .models import News
from .serializers import NewsSerializers
from rest_framework import generics

class NewsView(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializers