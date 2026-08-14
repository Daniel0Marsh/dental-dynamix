from django.urls import path
from .views import ServiceView



urlpatterns = [
    path("<slug:service>/", ServiceView.as_view(), name="service"),
]
