from django.urls import path
from django.shortcuts import redirect
from . views import ServicePageView

urlpatterns = [
    path('services/', ServicePageView.as_view(), name='services'),
]
