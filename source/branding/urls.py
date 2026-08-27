from django.urls import path
from . import views

urlpatterns = [
    # existing URLs...

    path(
        "remote-support/",
        views.remote_support,
        name="remote_support",
    ),
]