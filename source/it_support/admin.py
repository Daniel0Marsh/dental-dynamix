from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ITSupportPage


class SingletonAdmin(admin.ModelAdmin):
    """
    Base admin configuration for singleton models.
    Prevents adding multiple instances and redirects to the existing instance.
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
                    f"admin:{self.model._meta.app_label}_{self.model._meta.model_name}_change",
                    args=[instance.pk],
                )
            )
        return super().changelist_view(request, extra_context)

@admin.register(ITSupportPage)
class ITSupportPageAdmin(SingletonAdmin):
    readonly_fields = ("updated_at",)

    fieldsets = (
        ("Hero Section", {
            "fields": (
                "hero_image",
                "hero_image_alt_text",
                "hero_title",
                "hero_subtitle",
                "hero_primary_button_text",
            ),
        }),
        ("Overview", {
            "fields": (
                "overview_eyebrow",
                "overview_heading",
                "overview_description",
                "card_link_text",
            ),
        }),
        ("IT Support", {
            "fields": (
                "support_title",
                "support_description",
                "support_image",
                "support_image_alt",
            ),
        }),
        ("IT Protect", {
            "fields": (
                "protect_title",
                "protect_description",
                "protect_image",
                "protect_image_alt",
            ),
        }),
        ("Backup", {
            "fields": (
                "backup_title",
                "backup_description",
                "backup_image",
                "backup_image_alt",
            ),
        }),
        ("Final Call to Action", {
            "fields": (
                "final_cta_eyebrow",
                "final_cta_title",
                "final_cta_description",
                "final_cta_button_text",
            ),
        }),
        ("Admin Details", {
            "fields": ("updated_at",),
        }),
    )

    def has_add_permission(self, request):
        return (
            not self.model.objects.exists()
            and super().has_add_permission(request)
        )

    def changelist_view(self, request, extra_context=None):
        instance = self.model.objects.first()
        if instance:
            return HttpResponseRedirect(
                reverse(
                    "admin:it_support_itsupportpage_change",
                    args=[instance.pk],
                )
            )
        return super().changelist_view(request, extra_context)
    