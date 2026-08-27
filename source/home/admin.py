
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import HomePage, TermsAndConditionsPage


class SingletonAdmin(admin.ModelAdmin):
    """
    Base admin for pages that should only have one instance.
    """

    def has_add_permission(self, request):
        return not self.model.objects.exists()

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

        return super().changelist_view(request, extra_context)


@admin.register(HomePage)
class HomePageAdmin(SingletonAdmin):

    save_on_top = True

    fieldsets = (

        # =====================================================
        # 1. HERO
        # =====================================================

        (
            "1. Hero",
            {
                "description": (
                    "Main content displayed in the homepage hero area."
                ),
                "fields": (
                    "hero_image",
                    "hero_image_alt_text",
                    "hero_title",
                    "hero_subtitle",
                ),
            },
        ),

        # =====================================================
        # 2. SERVICES
        # =====================================================

        (
            "2. Services",
            {
                "classes": ("collapse",),
                "description": (
                    "Introductory content and the three fixed service cards."
                ),
                "fields": (
                    # -------------------------------------------------
                    # Section Content
                    # -------------------------------------------------

                    "services_eyebrow",
                    "services_title",
                    "services_description",

                    # -------------------------------------------------
                    # Service Card 1
                    # -------------------------------------------------

                    "service_card_1_title",
                    "service_card_1_description",
                    "service_card_1_image",
                    "service_card_1_image_alt_text",

                    # -------------------------------------------------
                    # Service Card 2
                    # -------------------------------------------------

                    "service_card_2_title",
                    "service_card_2_description",
                    "service_card_2_image",
                    "service_card_2_image_alt_text",

                    # -------------------------------------------------
                    # Service Card 3
                    # -------------------------------------------------

                    "service_card_3_title",
                    "service_card_3_description",
                    "service_card_3_image",
                    "service_card_3_image_alt_text",
                ),
            },
        ),

        # =====================================================
        # 3. FEATURED PRODUCTS
        # =====================================================

        (
            "3. Featured Products",
            {
                "classes": ("collapse",),
                "description": (
                    "Content displayed above the featured product listings."
                ),
                "fields": (
                    "featured_products_eyebrow",
                    "featured_products_title",
                    "featured_products_description",
                    "featured_products_empty_text",
                ),
            },
        ),

        # =====================================================
        # 4. DIGITAL DENTISTRY / IMAGING
        # =====================================================

        (
            "4. Digital Dentistry / Imaging",
            {
                "classes": ("collapse",),
                "description": (
                    "Content and image for the digital dentistry and "
                    "imaging section."
                ),
                "fields": (
                    "imaging_eyebrow",
                    "imaging_title",
                    "imaging_description",
                    "imaging_image",
                    "imaging_image_alt_text",
                ),
            },
        ),

        # =====================================================
        # 5. PRACTICE TECHNOLOGY
        # =====================================================

        (
            "5. Practice Technology",
            {
                "classes": ("collapse",),
                "description": (
                    "Content for the six fixed practice technology cards."
                ),
                "fields": (
                    # -------------------------------------------------
                    # Section Content
                    # -------------------------------------------------

                    "practice_technology_eyebrow",
                    "practice_technology_title",
                    "practice_technology_description",

                    # -------------------------------------------------
                    # Technology Card 1
                    # -------------------------------------------------

                    "practice_technology_card_1_icon",
                    "practice_technology_card_1_title",
                    "practice_technology_card_1_description",

                    # -------------------------------------------------
                    # Technology Card 2
                    # -------------------------------------------------

                    "practice_technology_card_2_icon",
                    "practice_technology_card_2_title",
                    "practice_technology_card_2_description",

                    # -------------------------------------------------
                    # Technology Card 3
                    # -------------------------------------------------

                    "practice_technology_card_3_icon",
                    "practice_technology_card_3_title",
                    "practice_technology_card_3_description",

                    # -------------------------------------------------
                    # Technology Card 4
                    # -------------------------------------------------

                    "practice_technology_card_4_icon",
                    "practice_technology_card_4_title",
                    "practice_technology_card_4_description",

                    # -------------------------------------------------
                    # Technology Card 5
                    # -------------------------------------------------

                    "practice_technology_card_5_icon",
                    "practice_technology_card_5_title",
                    "practice_technology_card_5_description",

                    # -------------------------------------------------
                    # Technology Card 6
                    # -------------------------------------------------

                    "practice_technology_card_6_icon",
                    "practice_technology_card_6_title",
                    "practice_technology_card_6_description",
                ),
            },
        ),

        # =====================================================
        # 6. COMPLETE SOLUTION
        # =====================================================

        (
            "6. Complete Solution",
            {
                "classes": ("collapse",),
                "description": (
                    "Content for the complete technology solution section "
                    "and its four fixed cards."
                ),
                "fields": (
                    # -------------------------------------------------
                    # Section Content
                    # -------------------------------------------------

                    "complete_solution_eyebrow",
                    "complete_solution_title",
                    "complete_solution_description",

                    # -------------------------------------------------
                    # Solution Card 1
                    # -------------------------------------------------

                    "complete_solution_card_1_icon",
                    "complete_solution_card_1_title",

                    # -------------------------------------------------
                    # Solution Card 2
                    # -------------------------------------------------

                    "complete_solution_card_2_icon",
                    "complete_solution_card_2_title",

                    # -------------------------------------------------
                    # Solution Card 3
                    # -------------------------------------------------

                    "complete_solution_card_3_icon",
                    "complete_solution_card_3_title",

                    # -------------------------------------------------
                    # Solution Card 4
                    # -------------------------------------------------

                    "complete_solution_card_4_icon",
                    "complete_solution_card_4_title",
                ),
            },
        ),

        # =====================================================
        # 7. TECHNOLOGY PARTNERS
        # =====================================================

        (
            "7. Technology Partners",
            {
                "classes": ("collapse",),
                "description": (
                    "Heading and introduction for the technology partners."
                ),
                "fields": (
                    "partners_eyebrow",
                    "partners_title",
                    "partners_description",
                    "partners_empty_text",
                ),
            },
        ),

        # =====================================================
        # 8. FINAL CALL TO ACTION
        # =====================================================

        (
            "8. Final Call to Action",
            {
                "classes": ("collapse",),
                "description": (
                    "Content displayed in the final contact section "
                    "at the bottom of the homepage."
                ),
                "fields": (
                    "final_cta_eyebrow",
                    "final_cta_title",
                    "final_cta_description",
                ),
            },
        ),

        # =====================================================
        # 9. SYSTEM
        # =====================================================

        (
            "9. System",
            {
                "classes": ("collapse",),
                "description": (
                    "System-managed information. These fields should "
                    "normally not need to be changed."
                ),
                "fields": (
                    "updated_at",
                ),
            },
        ),
    )

    readonly_fields = (
        "updated_at",
    )


@admin.register(TermsAndConditionsPage)
class TermsAndConditionsAdmin(SingletonAdmin):

    fieldsets = (
        (
            "Page Content",
            {
                "fields": (
                    "title",
                    "content",
                    "pdf",
                ),
            },
        ),
    )
