from .models import Partner


def partners(request):
    nav_partners = Partner.objects.filter(
        active=True
    ).only(
        "name",
        "slug",
        "display_order",
    )

    return {
        "nav_partners": nav_partners,
    }