from django.urls import path

from .views import ITSupportPageView


urlpatterns = [
    path(
        "it-support/",
        ITSupportPageView.as_view(),
        name="it_support",
    ),
]