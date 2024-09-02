from .models import Tweet
from .serializers import TweetSerializers
from rest_framework import generics

class TweetViews(generics.ListCreateAPIView):
    queryset = Tweet.objects.all()
    serializer_class = TweetSerializers