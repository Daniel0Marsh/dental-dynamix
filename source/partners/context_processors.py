from .models import Partner, PartnerProduct


def partners(request):
    nav_partners = Partner.objects.filter(
        active=True,
    ).only(
        "name",
        "slug",
        "display_order",
    )

    populated_categories = set(
        PartnerProduct.objects.filter(
            active=True,
            partner__active=True,
        )
        .order_by()
        .values_list("category", flat=True)
        .distinct()
    )

    nav_categories = [
        {"slug": slug, "name": name}
        for slug, name in PartnerProduct.CATEGORY_CHOICES
        if slug in populated_categories
    ]

    return {
        "nav_partners": nav_partners,
        "nav_categories": nav_categories,
        "partners": Partner.objects.filter(active=True),
    }