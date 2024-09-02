from django.urls import path,include
from .views import Bio

urlpatterns = [
    path('', Bio.as_view(), name='bio-list'),
]
