from django.views.generic import TemplateView
from .models import ServicePage


class ServicePageView(TemplateView):
    """
    View for displaying the Service page.
    """
    template_name = "services.html"

    def get_context_data(self, **kwargs):
        """
        Get context data for the template.
        """
        context = super().get_context_data(**kwargs)

        context.update({
            "service": ServicePage.objects.first(),
        })

        return context
    