from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView

from .models import ITSupportPage


class ITSupportPageView(TemplateView):
    template_name = "it_support.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        page = get_object_or_404(
            ITSupportPage,
            pk=1,
        )

        context["page"] = page
        context["offerings"] = [
            {
                "title": page.support_title,
                "description": page.support_description,
                "image": page.support_image,
                "image_alt": page.support_image_alt,
                "icon": "bi-headset",
            },
            {
                "title": page.protect_title,
                "description": page.protect_description,
                "image": page.protect_image,
                "image_alt": page.protect_image_alt,
                "icon": "bi-shield-check",
            },
            {
                "title": page.backup_title,
                "description": page.backup_description,
                "image": page.backup_image,
                "image_alt": page.backup_image_alt,
                "icon": "bi-cloud-arrow-up",
            },
        ]
        return context
