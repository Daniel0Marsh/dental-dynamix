from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import HttpRequest
from django.template import Context
from typing import Dict, Any
from .models import HomePage, PrivacyPolicyPage
from about.models import Testimonial
from branding.models import Branding


@method_decorator(never_cache, name='dispatch')
class HomePageView(TemplateView):
    """
    View for rendering the home page.

    Attributes:
        template_name (str): Name of the template file to be used.
    """
    template_name = 'home.html'

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        """
        Get the context data for rendering the template.

        Returns:
            Dict[str, Any]: Context data for the template.
        """

        home_page = HomePage.objects.first()

        # Build a list of 3 service cards
        service_cards = [
            {
                "title": home_page.service_card_1_title,
                "description": home_page.service_card_1_description,
                "image": home_page.service_card_1_image,
            },
            {
                "title": home_page.service_card_2_title,
                "description": home_page.service_card_2_description,
                "image": home_page.service_card_2_image,
            },
            {
                "title": home_page.service_card_3_title,
                "description": home_page.service_card_3_description,
                "image": home_page.service_card_3_image,
            },
        ]

        context = {
            "branding": Branding.objects.first(),
            "home": HomePage.objects.first(),
            "testimonials":  Testimonial.objects.filter(is_active=True),
            "service_cards": service_cards,
        }
        return context

class PrivacyPolicyPageView(TemplateView):
    """
    View for displaying privacy policy.
    """
    template_name = 'privacy_policy.html'

    def get_context_data(self, **kwargs):
        """
        Get context data for the template.
        """

        context = {
            "branding": Branding.objects.first(),
            "home": HomePage.objects.first(),
            'privacy_policy': PrivacyPolicyPage.objects.first(),
        }
        return context
