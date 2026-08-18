from django.views.generic import TemplateView
from .models import OurSolutionsPage
from home.models import HomePage


class OurSolutionsPageView(TemplateView):
    """
    View for displaying the Our Solutions page.
    """
    template_name = "oursolutions.html"

    def get_context_data(self, **kwargs):
        """
        Get context data for the template.
        """
        context = super().get_context_data(**kwargs)

        context.update({
            "home": HomePage.objects.first(),
            "solutions": OurSolutionsPage.objects.first(),
        })

        return context
    