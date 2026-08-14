from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView
from . views import HomePageView, PrivacyPolicyPageView


def redirect_to_sovereign101_consultation(request):
    return redirect('https://sovereign101.com/bitcoin-consultation/', permanent=True)


def redirect_to_sovereign101_hardware(request):
    return redirect('https://sovereign101.com/bitcoin-hardware/', permanent=True)


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('privacy-policy/', PrivacyPolicyPageView.as_view(), name='privacy_policy'),
    # Temporary redirects for broken blog posts
    path('bitcoin-consultation/', redirect_to_sovereign101_consultation, name='bitcoin_consultation'),
    path('bitcoin-hardware/', redirect_to_sovereign101_hardware, name='bitcoin_hardware'),
]

urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]