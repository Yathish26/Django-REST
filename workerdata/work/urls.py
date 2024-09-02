
from django.urls import path
from .views import WorkerViews

urlpatterns = [
    path('',WorkerViews.as_view(),name='worker-views')
]
