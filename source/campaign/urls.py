from django.urls import path
from django.shortcuts import redirect
from django.views.generic import TemplateView
from . views import CampaignPageView


urlpatterns = [
    path('campaign/', CampaignPageView.as_view(), name='campaign'),
]
