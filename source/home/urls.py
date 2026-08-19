from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView
from . views import HomePageView, PrivacyPolicyPageView


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('privacy-policy/', PrivacyPolicyPageView.as_view(), name='privacy_policy'),
]

urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
