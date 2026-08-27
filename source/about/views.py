from django.views.generic import TemplateView
from .models import AboutPage
from home.models import HomePage
from partners.models import Partner


class AboutUsPageView(TemplateView):
    """
    View for displaying the About Us page.
    """
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        """
        Get context data for the template.
        """
        context = super().get_context_data(**kwargs)

        context.update({
            "home": HomePage.objects.first(),
            "about": AboutPage.objects.first(),
            "partners": Partner.objects.filter(
                active=True
            ),
        })

        return context
    