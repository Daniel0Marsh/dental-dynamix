from django.urls import path
from django.shortcuts import redirect
from . views import AboutUsPageView, TestimonialsPageView

urlpatterns = [
    path('about/', AboutUsPageView.as_view(), name='about'),
    path('testimonials/', TestimonialsPageView.as_view(), name='testimonials'),
]
