from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.views.generic import TemplateView

from branding.models import Branding
from home.views import HomePage
from .models import BlogPage, BlogPost


class BlogPageView(TemplateView):
    """Display the blog hero and published posts."""

    template_name = 'blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            'branding': Branding.objects.first(),
            'page': BlogPage.objects.first(),
            'blogs': BlogPost.objects.filter(
                published=True,
            ).order_by('-created_at'),
        })
        return context


class BlogDetailsPageView(TemplateView):
    """Display a published blog post."""

    template_name = 'blog_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        published_posts = BlogPost.objects.filter(published=True)

        blog = get_object_or_404(
            published_posts,
            slug=self.kwargs['blog_slug'],
        )

        context.update({
            'branding': Branding.objects.first(),
            'home': HomePage.objects.first(),
            'blog': blog,
            'recent_posts': published_posts.exclude(
                pk=blog.pk,
            ).order_by('-created_at')[:5],
            'current_date': timezone.now(),
            'meta': blog.meta,
        })
        return context
    