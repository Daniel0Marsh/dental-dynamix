from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import StaticViewSitemap, ServiceSitemap

# Sitemap configuration
sitemaps = {
    'static': StaticViewSitemap,
    'services': ServiceSitemap,
}

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('about.urls')),
    path('', include('contact.urls')),
    path('', include('services.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='sitemap'),
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# configure admin titles
admin.site.site_header = "welcome to Dental Dynamix Admin"
admin.site.site_title = "Dental Dynamix"
admin.site.index_title = "Welcome to the admin area"

# Error handlers
handler400 = 'errors.views.handler400'
handler403 = 'errors.views.handler403'
handler404 = 'errors.views.handler404'
handler500 = 'errors.views.handler500'
