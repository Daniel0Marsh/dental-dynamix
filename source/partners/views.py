from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import (
    Partner,
    PartnerProduct,
    ProductCategory,
    ProductPage,
)


def partner_list(request):

    partners = Partner.objects.filter(
        active=True
    )

    return render(
        request,
        "partners.html",
        {
            "partners": partners,
        },
    )


def _get_product_catalogue(request, partner=None):
    """
    Build the product catalogue.

    If a partner is supplied, the catalogue is restricted
    to that partner. Otherwise, all active partner products
    are shown.

    Search and category filters are then applied.
    """

    # ---------------------------------------------------------
    # BASE PRODUCT QUERY
    # ---------------------------------------------------------

    products = (
        PartnerProduct.objects
        .filter(
            active=True,
            partner__active=True,
        )
        .select_related(
            "partner",
            "category",
        )
    )

    # ---------------------------------------------------------
    # PARTNER FILTER
    # ---------------------------------------------------------

    if partner:

        products = products.filter(
            partner=partner
        )

    # ---------------------------------------------------------
    # SEARCH
    # ---------------------------------------------------------

    query = request.GET.get(
        "q",
        ""
    ).strip()

    if query:

        products = products.filter(
            Q(name__icontains=query)
            | Q(description__icontains=query)
        )

    # ---------------------------------------------------------
    # CATEGORY FILTER
    # ---------------------------------------------------------

    category_slug = request.GET.get(
        "category",
        ""
    ).strip()

    if category_slug:

        products = products.filter(
            category__slug=category_slug
        )

    # ---------------------------------------------------------
    # ORDERING
    # ---------------------------------------------------------

    products = products.order_by(
        "category__display_order",
        "category__name",
        "display_order",
        "name",
    )

    # ---------------------------------------------------------
    # AVAILABLE CATEGORIES
    #
    # These are restricted to the currently selected partner.
    # ---------------------------------------------------------

    category_products = (
        PartnerProduct.objects
        .filter(
            active=True,
            partner__active=True,
        )
    )

    if partner:

        category_products = category_products.filter(
            partner=partner
        )

    categories = (
        ProductCategory.objects
        .filter(
            active=True,
            products__in=category_products,
        )
        .distinct()
        .order_by(
            "display_order",
            "name",
        )
    )

    # ---------------------------------------------------------
    # PARTNERS
    #
    # Used by the partner selector.
    # ---------------------------------------------------------

    partners = Partner.objects.filter(
        active=True
    ).order_by(
        "display_order",
        "name",
    )

    return {
        "products": products,
        "categories": categories,
        "partners": partners,
        "query": query,
        "selected_category": category_slug,
    }


def partner_detail(request, slug):
    """
    Display the catalogue filtered to a specific partner.
    """

    partner = get_object_or_404(
        Partner,
        slug=slug,
        active=True,
    )

    catalogue = _get_product_catalogue(
        request,
        partner=partner,
    )

    seo_title = (
        partner.seo_title
        or f"{partner.name} | Dental Dynamix"
    )

    seo_description = (
        partner.seo_description
        or partner.hero_subtitle
    )

    return render(
        request,
        "products.html",
        {
            **catalogue,

            "partner": partner,

            "seo_title": seo_title,
            "seo_description": seo_description,
        },
    )


def product_list(request):
    """
    Display the complete product catalogue.

    The ProductPage model provides the editable hero
    and SEO content for the All Products page.
    """

    catalogue = _get_product_catalogue(
        request
    )

    product_page = ProductPage.objects.first()

    if product_page:

        seo_title = (
            product_page.seo_title
            or product_page.hero_title
            or "Dental Products | Dental Dynamix"
        )

        seo_description = (
            product_page.seo_description
            or product_page.hero_subtitle
        )

    else:

        seo_title = (
            "Dental Products | Dental Dynamix"
        )

        seo_description = (
            "Explore dental imaging equipment, "
            "technology and solutions from "
            "leading dental technology partners."
        )

    return render(
        request,
        "products.html",
        {
            **catalogue,

            "partner": None,

            "product_page": product_page,

            "seo_title": seo_title,
            "seo_description": seo_description,
        },
    )