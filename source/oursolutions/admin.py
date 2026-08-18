from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import OurSolutionsPage


class SingletonAdmin(admin.ModelAdmin):
    """
    Base admin configuration for singleton models.

    Prevents multiple instances from being created and redirects
    the changelist to the existing instance.
    """

    def has_add_permission(self, request):
        if self.model.objects.exists():
            return False

        return super().has_add_permission(request)

    def changelist_view(self, request, extra_context=None):
        instance = self.model.objects.first()

        if instance:
            return HttpResponseRedirect(
                reverse(
                    f"admin:{self.model._meta.app_label}_"
                    f"{self.model._meta.model_name}_change",
                    args=[instance.pk],
                )
            )

        return super().changelist_view(
            request,
            extra_context,
        )


@admin.register(OurSolutionsPage)
class OurSolutionsPageAdmin(SingletonAdmin):
    """
    Admin configuration for the Our Solutions page singleton.
    """

    fieldsets = (

        # =====================================================
        # Hero
        # =====================================================

        (
            "Hero Section",
            {
                "fields": (
                    "hero_image",
                    "hero_image_alt_text",
                    "hero_title",
                    "hero_subtitle",
                )
            },
        ),

        # =====================================================
        # IT & Practice Infrastructure
        # =====================================================

        (
            "IT & Practice Infrastructure",
            {
                "fields": (
                    "it_image",
                    "it_image_alt_text",
                    "it_title",
                    "it_text",
                )
            },
        ),

        # =====================================================
        # Dental Imaging & Digital Dentistry
        # =====================================================

        (
            "Dental Imaging & Digital Dentistry",
            {
                "fields": (
                    "imaging_image",
                    "imaging_image_alt_text",
                    "imaging_title",
                    "imaging_text",
                )
            },
        ),

        # =====================================================
        # Supply, Installation & Integration
        # =====================================================

        (
            "Supply, Installation & Integration",
            {
                "fields": (
                    "installation_image",
                    "installation_image_alt_text",
                    "installation_title",
                    "installation_text",
                )
            },
        ),

        # =====================================================
        # Software & Digital Workflows
        # =====================================================

        (
            "Software & Digital Workflows",
            {
                "fields": (
                    "software_image",
                    "software_image_alt_text",
                    "software_title",
                    "software_text",
                )
            },
        ),

        # =====================================================
        # Ongoing Support
        # =====================================================

        (
            "Ongoing Support",
            {
                "fields": (
                    "support_image",
                    "support_image_alt_text",
                    "support_title",
                    "support_text",
                )
            },
        ),
    )