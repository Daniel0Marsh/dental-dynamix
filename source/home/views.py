from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import HttpRequest
from django.template import Context
from typing import Dict, Any
from .models import HomePage, TermsAndConditionsPage
from partners.models import PartnerProduct
from branding.models import Branding


@method_decorator(never_cache, name="dispatch")
class HomePageView(TemplateView):
    """
    View for rendering the home page.
    """

    template_name = "home-v2.html"

    def get_context_data(self, **kwargs) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)

        home_page = HomePage.objects.first()

        # Products selected for the homepage
        featured_products = (
            PartnerProduct.objects
            .filter(
                active=True,
                show_on_homepage=True,
                partner__active=True,
            )
            .select_related("partner")
            .order_by(
                "homepage_order",
                "name",
            )
        )

        context.update({
            "branding": Branding.objects.first(),
            "home": home_page,
            "featured_products": featured_products,
        })

        return context


class TermsAndConditionsView(TemplateView):
    """
    View for displaying terms and conditions.
    """
    template_name = 'terms_and_conditions.html'

    def get_context_data(self, **kwargs):
        """
        Get context data for the template.
        """

        context = {
            "home": HomePage.objects.first(),
            'terms_and_conditions': TermsAndConditionsPage.objects.first(),
        }
        return context
