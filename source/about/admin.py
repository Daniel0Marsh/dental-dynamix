from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import AboutPage, Testimonial


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


@admin.register(AboutPage)
class AboutPageAdmin(SingletonAdmin):
    """
    Admin configuration for the About page singleton.
    """

    fieldsets = (
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
            "Mission Section",
            {
                "fields": (
                    "mission_image",
                    "mission_title",
                    "mission_text",
                )
            },
        ),
        (
            "Values Section",
            {
                "fields": (
                    "values_image",
                    "values_title",
                    "values_text",
                )
            },
        ),
        (
            "Our Team Section",
            {
                "fields": (
                    "team_image",
                    "team_title",
                    "team_text",
                )
            },
        ),
    )


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = (
        "author_name",
        "author_company",
        "is_active",
        "display_order",
        "created_at",
    )
    list_editable = ("is_active", "display_order")
    list_filter = ("is_active",)
    search_fields = ("author_name", "quote", "author_company")
    ordering = ("display_order", "created_at")
