from django.urls import path

from .views import BlogPageView, BlogDetailsPageView


urlpatterns = [
    path('blog/', BlogPageView.as_view(), name='blog'),
    path(
        'blog/<slug:blog_slug>/',
        BlogDetailsPageView.as_view(),
        name='blog_details',
    ),
]