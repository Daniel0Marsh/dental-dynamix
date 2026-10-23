
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import ServicePage


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


@admin.register(ServicePage)
class ServicePageAdmin(SingletonAdmin):
    """
    Admin configuration for the Service page singleton.
    Organises page content into expandable sections.
    """

    readonly_fields = ("updated_at",)

    fieldsets = (
        (
            "Hero Section",
            {
                "classes": ("collapse",),
                "fields": (
                    "hero_image",
                    "hero_image_alt_text",
                    "hero_title",
                    "hero_subtitle",
                    "hero_primary_button_text",
                ),
            },
        ),
        (
            "Trust Strip",
            {
                "classes": ("collapse",),
                "fields": (
                    ("trust_1_title", "trust_1_icon"),
                    "trust_1_description",
                    ("trust_2_title", "trust_2_icon"),
                    "trust_2_description",
                    ("trust_3_title", "trust_3_icon"),
                    "trust_3_description",
                    ("trust_4_title", "trust_4_icon"),
                    "trust_4_description",
                ),
            },
        ),
        (
            "Services Overview",
            {
                "classes": ("collapse",),
                "fields": (
                    "overview_eyebrow",
                    "overview_heading",
                    "overview_description",
                    (
                        "overview_1_title",
                        "overview_1_image",
                    ),
                    "overview_1_image_alt",
                    "overview_1_icon",
                    "overview_1_description",
                    "overview_1_link_text",
                    (
                        "overview_2_title",
                        "overview_2_image",
                    ),
                    "overview_2_image_alt",
                    "overview_2_icon",
                    "overview_2_description",
                    "overview_2_link_text",
                    (
                        "overview_3_title",
                        "overview_3_image",
                    ),
                    "overview_3_image_alt",
                    "overview_3_icon",
                    "overview_3_description",
                    "overview_3_link_text",
                ),
            },
        ),
        (
            "Critical Examinations",
            {
                "classes": ("collapse",),
                "fields": (
                    "critical_eyebrow",
                    "critical_title",
                    "critical_description",
                    "critical_secondary_description",
                    "critical_bullet_1",
                    "critical_bullet_2",
                    "critical_bullet_3",
                    "critical_card_icon",
                    "critical_card_title",
                    "critical_card_description",
                    "critical_button_text",
                    "critical_card_note",
                ),
            },
        ),
        (
            "Our Approach / Process",
            {
                "classes": ("collapse",),
                "fields": (
                    "approach_eyebrow",
                    "approach_title",
                    "approach_description",
                    (
                        "approach_step_1_number",
                        "approach_step_1_title",
                    ),
                    "approach_step_1_description",
                    (
                        "approach_step_2_number",
                        "approach_step_2_title",
                    ),
                    "approach_step_2_description",
                    (
                        "approach_step_3_number",
                        "approach_step_3_title",
                    ),
                    "approach_step_3_description",
                ),
            },
        ),
        (
            "Preparing Your Enquiry",
            {
                "classes": ("collapse",),
                "fields": (
                    "enquiry_eyebrow",
                    "enquiry_heading",
                    "enquiry_description",
                    ("enquiry_1_title", "enquiry_1_icon"),
                    "enquiry_1_description",
                    ("enquiry_2_title", "enquiry_2_icon"),
                    "enquiry_2_description",
                    ("enquiry_3_title", "enquiry_3_icon"),
                    "enquiry_3_description",
                    "enquiry_image",
                    "enquiry_image_alt",
                ),
            },
        ),
        (
            "Final Call to Action",
            {
                "classes": ("collapse",),
                "fields": (
                    "final_cta_eyebrow",
                    "final_cta_title",
                    "final_cta_description",
                    "final_cta_button_text",
                ),
            },
        ),
        (
            "Admin Details",
            {
                "classes": ("collapse",),
                "fields": ("updated_at",),
            },
        ),
    )

    def has_delete_permission(self, request, obj=None):
        """Prevent deletion of the singleton page."""
        return False
