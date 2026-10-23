from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView
from . views import HomePageView, TermsAndConditionsView


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path('terms-and-conditions/', TermsAndConditionsView.as_view(), name='terms_and_conditions'),
]

urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
