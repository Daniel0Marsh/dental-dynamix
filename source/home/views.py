from django.views.generic import TemplateView
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.http import HttpRequest
from django.http import Http404
from django.shortcuts import get_object_or_404
from django.template import Context
from typing import Dict, Any
from .models import HomePage, LegalPage
from campaign.models import CampaignPage
from partners.models import PartnerProduct
from branding.models import Branding


@method_decorator(never_cache, name="dispatch")
class HomePageView(TemplateView):
    """
    View for rendering the home page.
    """

    template_name = "home.html"

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
            "campaign": CampaignPage.objects.first(),
        })

        return context


class LegalPageView(TemplateView):
    template_name = "policy_page.html"
    page_type = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        policy = get_object_or_404(
            LegalPage,
            page_type=self.page_type,
        )

        if not policy.pdf:
            raise Http404("Policy document is not available.")

        context.update({
            "home": HomePage.objects.first(),
            "policy": policy,
        })
        return context