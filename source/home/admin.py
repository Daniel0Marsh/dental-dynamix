from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import HomePage, PrivacyPolicyPage


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


@admin.register(HomePage)
class HomePageAdmin(SingletonAdmin):
    fieldsets = (
        ("Hero Section", {
            "fields": ("hero_image", "hero_subtitle")
        }),
        ("Service Cards Section", {
            "fields": (
                ("service_card_1_title", "service_card_1_description"),
                "service_card_1_image",

                ("service_card_2_title", "service_card_2_description"),
                "service_card_2_image",

                ("service_card_3_title", "service_card_3_description"),
                "service_card_3_image",
            )
        }),
        ("About Section", {
            "fields": ("about_image", "about_title", "about_copy")
        }),
        ("Testimonial Section", {
            "fields": ("testimonial_image",)
        }),
        ("Support Section", {
            "fields": ("support_image", "support_title", "support_copy")
        }),
    )


@admin.register(PrivacyPolicyPage)
class PrivacyPolicyAdmin(SingletonAdmin):
    pass