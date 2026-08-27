from django.db.models import Q
from django.shortcuts import get_object_or_404, render

from .models import (
    Partner,
    PartnerProduct,
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

    products = (
        PartnerProduct.objects
        .filter(
            active=True,
            partner__active=True,
        )
        .select_related(
            "partner",
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
            category=category_slug
        )

    # ---------------------------------------------------------
    # ORDERING
    # ---------------------------------------------------------

    products = products.order_by(
        "category",
        "display_order",
        "name",
    )

    # ---------------------------------------------------------
    # CATEGORY CHOICES
    # ---------------------------------------------------------

    categories = [
        {
            "slug": slug,
            "name": name,
        }
        for slug, name in PartnerProduct.CATEGORY_CHOICES
    ]

    # ---------------------------------------------------------
    # PARTNERS
    # ---------------------------------------------------------

    partners = (
        Partner.objects
        .filter(
            active=True
        )
        .order_by(
            "display_order",
            "name",
        )
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


def product_detail(request, partner_slug, slug):
    """
    Display the detailed product page.
    """

    product = get_object_or_404(
        PartnerProduct.objects
        .select_related(
            "partner",
        )
        .prefetch_related(
            "gallery_images",
            "documents",
            "specifications",
        ),
        slug=slug,
        partner__slug=partner_slug,
        active=True,
        partner__active=True,
    )

    gallery_images = list(
        product.gallery_images.all()
    )

    documents = [
        document
        for document in product.documents.all()
        if document.active
    ]

    specifications = list(
        product.specifications.all()
    )

    seo_title = (
        f"{product.name} | "
        f"{product.partner.name} | "
        "Dental Dynamix"
    )

    seo_description = (
        product.description
        or product.detailed_description
        or (
            f"Learn more about {product.name} from "
            f"{product.partner.name}."
        )
    )

    features = [
        feature.strip()
        for feature in product.features.splitlines()
        if feature.strip()
    ]

    return render(
        request,
        "product_detail.html",
        {
            "product": product,
            "gallery_images": gallery_images,
            "documents": documents,
            "specifications": specifications,
            "features": features,
            "seo_title": seo_title,
            "seo_description": seo_description,
        },
    )