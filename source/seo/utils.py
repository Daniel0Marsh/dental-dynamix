from django.utils.html import strip_tags
from django.utils.text import Truncator

from .models import PageSEO


SITE_URL = "https://dentaldynamix.co.uk"


def build_meta(request, title, description):
    """
    Prefer an existing admin SEO entry.
    Otherwise generate metadata from the page content.
    """
    seo = PageSEO.objects.filter(url_path=request.path).first()

    if seo:
        return seo.meta

    description = Truncator(
        " ".join(strip_tags(description or "").split())
    ).chars(160)

    return {
        "title": title,
        "description": description,
        "canonical_url": f"{SITE_URL}{request.path}",
        "robots": "index, follow",
        "og_title": title,
        "og_description": description,
        "og_type": "website",
        "og_locale": "en_GB",
        "site_name": "Dental Dynamix",
        "twitter_title": title,
        "twitter_description": description,
        "twitter_card": "summary",
    }
