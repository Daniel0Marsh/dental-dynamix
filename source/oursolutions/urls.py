from django.urls import path
from django.shortcuts import redirect
from . views import OurSolutionsPageView

urlpatterns = [
    path('oursolutions/', OurSolutionsPageView.as_view(), name='oursolutions'),
]
