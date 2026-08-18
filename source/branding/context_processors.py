from .models import Branding


def branding(request):
    """
    Make the website Branding object available to all templates.
    """
    branding = Branding.objects.first()

    return {
        "branding": branding,
    }