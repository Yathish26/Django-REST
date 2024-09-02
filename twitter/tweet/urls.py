from django.urls import path
from .views import TweetViews

urlpatterns = [
    path('',TweetViews.as_view()),
]