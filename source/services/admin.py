from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ServicePage


@admin.register(ServicePage)
class ServicePageAdmin(admin.ModelAdmin):
    """
    Admin configuration for Service pages.
    Enforces one page per service type.
    """

    list_display = ("service",)
    list_filter = ("service",)
    ordering = ("service",)

    fieldsets = (
        (
            "Service",
            {
                "fields": ("service",),
            },
        ),
        (
            "Hero Section",
            {
                "fields": (
                    "hero_image",
                    "hero_title",
                    "hero_subtitle",
                )
            },
        ),
        (
            "Info Section",
            {
                "fields": (
                    "info_image",
                    "info_title",
                    "info_text",
                )
            },
        ),
        (
            "Support Section",
            {
                "fields": (
                    "support_image",
                    "support_title",
                    "support_text",
                )
            },
        ),
        (
            "Pricing Section",
            {
                "fields": (
                    "pricing_1_title",
                    "pricing_1_amount",
                    "pricing_1_support_text",
                    "pricing_2_title",
                    "pricing_2_amount",
                    "pricing_2_support_text",
                )
            },
        ),
    )
