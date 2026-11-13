from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import BlogPost
from partners.models import Partner, PartnerProduct


class StaticViewSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return [
            "home",
            "about",
            "services",
            "it_support",
            "contact",
            "campaign",
            "terms_and_conditions",
            "partners:list",
            "partners:products",
            "blog",
        ]

    def location(self, item):
        return reverse(item)


class BlogPostSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return BlogPost.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_at


class PartnerSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return Partner.objects.filter(active=True)

    def lastmod(self, obj):
        return obj.updated_at


class ProductSitemap(Sitemap):
    protocol = "https"

    def items(self):
        return (
            PartnerProduct.objects
            .filter(active=True, partner__active=True)
            .exclude(slug__isnull=True)
            .exclude(slug="")
            .select_related("partner")
        )