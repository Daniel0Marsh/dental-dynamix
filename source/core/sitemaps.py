from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from services.models import ServicePage

class StaticViewSitemap(Sitemap):
    priority = 0.8
    changefreq = 'monthly'

    def items(self):
        return ['home', 'about', 'testimonials', 'contact', 'privacy_policy']

    def location(self, item):
        return reverse(item)

class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.9

    def items(self):
        return BlogPost.objects.filter(published=True)

    def lastmod(self, obj):
        return obj.updated_at

class ServiceSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.7

    def items(self):
        return ServicePage.objects.all()

    def location(self, obj):
        return reverse('service', args=[obj.service])

    def lastmod(self, obj):
        return getattr(obj, 'updated_at', None)
