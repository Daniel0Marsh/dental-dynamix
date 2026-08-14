from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import HttpRequest
from django.template import Context
from typing import Dict, Any
from .models import Testimonial
from home.models import HomePage
from branding.models import Branding
from .models import AboutPage, Testimonial

class TestimonialsPageView(TemplateView):
    """
    View for displaying testimonials.
    """
    template_name = 'testimonials.html'
    def get_context_data(self, **kwargs):
        """
        Get context data for the template.
        """

        context = {
            "branding": Branding.objects.first(),
            "home": HomePage.objects.first(),
            'testimonials': Testimonial.objects.all(),
        }
        return context

class AboutUsPageView(TemplateView):
    """
    View for displaying testimonials.
    """
    template_name = 'about.html'
    def get_context_data(self, **kwargs):
        """
        Get context data for the template.
        """

        context = {
            "branding": Branding.objects.first(),
            "home": HomePage.objects.first(),
            "about": AboutPage.objects.first(),
            'testimonials': Testimonial.objects.all(),
        }
        return context