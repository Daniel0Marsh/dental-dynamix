from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView
from . views import HomePageView, LegalPageView


urlpatterns = [
    path('', HomePageView.as_view(), name="home"),
    path(
        "terms-and-conditions/",
        LegalPageView.as_view(page_type="terms"),
        name="terms_and_conditions",
    ),
    path(
        "privacy-policy/",
        LegalPageView.as_view(page_type="privacy"),
        name="privacy_policy",
    ),
    path(
        "cookie-policy/",
        LegalPageView.as_view(page_type="cookies"),
        name="cookie_policy",
    ),
]

urlpatterns += [
    path('robots.txt', TemplateView.as_view(template_name="robots.txt", content_type="text/plain")),
]
