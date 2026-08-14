from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

from branding.models import Branding
from home.models import HomePage
from .models import ServicePage


class ServiceView(TemplateView):
    template_name = "service.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        service = get_object_or_404(
            ServicePage,
            service=kwargs["service"],
        )

        context.update({
            "branding": Branding.objects.first(),
            "home": HomePage.objects.first(),
            "service": service,
        })

        return context
