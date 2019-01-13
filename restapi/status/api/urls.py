from django.contrib import admin
from django.urls import path
from .views import (
    StatusAPIView,
    # StatusListSearchAPIView,
    # StatusCreateAPIView,
    StatusDetailAPIView,
    # StatusDeleteAPIView,
    # StatusUpdateAPIView,
    # StatusDetailAPIView
)

urlpatterns = [
    path('',StatusAPIView.as_view()),
    path('<int:pk>/',StatusDetailAPIView.as_view()),
]
