from django.contrib import admin

from .models import (
    Partner,
    PartnerProduct,
    ProductCategory,
    ProductPage,
)


class PartnerProductInline(admin.TabularInline):

    model = PartnerProduct

    extra = 1

    fields = (
        "name",
        "category",
        "description",
        "image",
        "product_url",
        "active",
        "display_order",
    )


@admin.register(Partner)
class PartnerAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "active",
        "display_order",
        "created_at",
        "updated_at",
    )

    list_filter = (
        "active",
    )

    search_fields = (
        "name",
        "hero_title",
        "hero_subtitle",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    ordering = (
        "display_order",
        "name",
    )

    fieldsets = (
        (
            "Partner Information",
            {
                "fields": (
                    "name",
                    "slug",
                    "logo",
                    "website_url",
                )
            },
        ),
        (
            "Hero Section",
            {
                "fields": (
                    "hero_image",
                    "hero_title",
                    "hero_subtitle",
                ),
                "description": (
                    "This content is displayed prominently on "
                    "the partner page hero."
                ),
            },
        ),
        (
            "SEO",
            {
                "fields": (
                    "seo_title",
                    "seo_description",
                ),
            },
        ),
        (
            "Publishing",
            {
                "fields": (
                    "active",
                    "display_order",
                ),
            },
        ),
    )

    inlines = [
        PartnerProductInline,
    ]

@admin.register(ProductPage)
class ProductPageAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Hero Section",
            {
                "fields": (
                    "hero_image",
                    "hero_image_alt_text",
                    "hero_title",
                    "hero_subtitle",
                ),
                "description": (
                    "This content is displayed on the "
                    "main All Products page."
                ),
            },
        ),
        (
            "SEO",
            {
                "fields": (
                    "seo_title",
                    "seo_description",
                ),
            },
        ),
    )

    def has_add_permission(self, request):

        return not ProductPage.objects.exists()

    def has_delete_permission(self, request, obj=None):

        return False

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "active",
        "display_order",
    )

    list_filter = (
        "active",
    )

    search_fields = (
        "name",
        "description",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    ordering = (
        "display_order",
        "name",
    )


@admin.register(PartnerProduct)
class PartnerProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "partner",
        "category",
        "active",
        "display_order",
    )

    list_filter = (
        "partner",
        "category",
        "active",
    )

    search_fields = (
        "name",
        "description",
        "partner__name",
    )

    ordering = (
        "partner",
        "category",
        "display_order",
        "name",
    )