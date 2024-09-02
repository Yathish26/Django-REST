from rest_framework import generics
from .models import Workers
from .serializers import WorkerSerializers


class WorkerViews(generics.ListCreateAPIView):
    queryset = Workers.objects.all()
    serializer_class = WorkerSerializers