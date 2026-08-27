from django.contrib import admin

from .models import (
    Partner,
    PartnerProduct,
    PartnerProductDocument,
    PartnerProductImage,
    PartnerProductSpecification,
    ProductPage,
)



class PartnerProductImageInline(admin.TabularInline):

    model = PartnerProductImage

    extra = 1

    fields = (
        "image",
        "alt_text",
        "display_order",
    )

    ordering = (
        "display_order",
        "id",
    )


class PartnerProductDocumentInline(admin.TabularInline):

    model = PartnerProductDocument

    extra = 1

    fields = (
        "title",
        "document_type",
        "file",
        "active",
        "display_order",
    )

    ordering = (
        "display_order",
        "title",
    )


class PartnerProductSpecificationInline(admin.TabularInline):

    model = PartnerProductSpecification

    extra = 1

    fields = (
        "name",
        "value",
        "display_order",
    )

    ordering = (
        "display_order",
        "name",
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
                    "hero_image_alt_text",
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


@admin.register(PartnerProduct)
class PartnerProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "partner",
        "category",
        "active",
        "show_on_homepage",
        "homepage_order",
        "display_order",
    )

    list_filter = (
        "partner",
        "category",
        "active",
        "show_on_homepage",
    )

    search_fields = (
        "name",
        "description",
        "detailed_description",
        "partner__name",
    )

    prepopulated_fields = {
        "slug": ("name",),
    }

    list_editable = (
        "active",
        "show_on_homepage",
        "homepage_order",
    )

    ordering = (
        "homepage_order",
        "partner",
        "category",
        "display_order",
        "name",
    )

    fieldsets = (
        (
            "Product Information",
            {
                "fields": (
                    "partner",
                    "category",
                    "name",
                    "slug",
                    "description",
                    "detailed_description",
                    "features",
                    "image",
                    "product_url",
                ),
                "description": (
                    "Core product information used throughout "
                    "the website and on the product detail page."
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
        (
            "Homepage",
            {
                "fields": (
                    "show_on_homepage",
                    "homepage_order",
                ),
                "description": (
                    "Control whether this product appears in "
                    "the featured products section on the homepage."
                ),
            },
        ),
    )

    inlines = [
        PartnerProductImageInline,
        PartnerProductDocumentInline,
        PartnerProductSpecificationInline,
    ]