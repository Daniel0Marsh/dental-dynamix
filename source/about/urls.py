from django.urls import path
from django.shortcuts import redirect
from . views import AboutUsPageView

urlpatterns = [
    path('about/', AboutUsPageView.as_view(), name='about'),
]
