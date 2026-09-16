from django.urls import path

from .views import llms_txt


urlpatterns = [
    path("llms.txt", llms_txt, name="llms_txt"),
]