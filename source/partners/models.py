from django.db import models
from django.urls import reverse


class Partner(models.Model):
    name = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=200,
        unique=True
    )

    logo = models.ImageField(
        upload_to="partners/logos/",
        default="default/logo.svg",
        help_text="Upload the partner's logo image."
    )

    hero_image = models.ImageField(
        upload_to="partners/hero/",
        default="default/hero_image.webp",
        help_text="Upload the partner hero section image."
    )

    hero_image_alt_text = models.CharField(
        max_length=255,
        default="Dental technology and imaging solutions",
        help_text=(
            "Alternative text for the hero image for SEO "
            "and accessibility."
        )
    )

    hero_title = models.CharField(
        max_length=200,
        help_text=(
            "Main heading displayed on the partner hero."
        )
    )

    hero_subtitle = models.TextField(
        help_text=(
            "Short commercial description displayed below "
            "the partner hero heading."
        )
    )

    website_url = models.URLField(
        blank=True,
        help_text="The partner's own website."
    )

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        help_text=(
            "Optional custom SEO title. "
            "Leave blank to generate automatically."
        )
    )

    seo_description = models.TextField(
        blank=True,
        help_text=(
            "Optional custom SEO description. "
            "Leave blank to generate automatically."
        )
    )

    active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Partner"
        verbose_name_plural = "Partners"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            "partners:detail",
            kwargs={"slug": self.slug}
        )

class ProductPage(models.Model):
    hero_image = models.ImageField(
        upload_to="partners/catalogue/",
        default="default/hero_image.webp",
        help_text="Hero image displayed on the all products page."
    )

    hero_image_alt_text = models.CharField(
        max_length=255,
        default="Dental technology and imaging solutions",
        help_text=(
            "Alternative text for the hero image "
            "for SEO and accessibility."
        )
    )

    hero_title = models.CharField(
        max_length=200,
        default="Dental Products",
        help_text="Main heading displayed on the all products page."
    )

    hero_subtitle = models.TextField(
        default=(
            "Explore dental imaging equipment, technology "
            "and solutions from leading industry partners."
        ),
        help_text=(
            "Short description displayed below "
            "the hero heading."
        )
    )

    seo_title = models.CharField(
        max_length=200,
        blank=True,
        help_text="Optional custom SEO title."
    )

    seo_description = models.TextField(
        blank=True,
        help_text="Optional custom SEO description."
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    class Meta:
        verbose_name = "Product Page"
        verbose_name_plural = "Product Page"

    def __str__(self):
        return "All Products Page"

    def save(self, *args, **kwargs):
        if not self.pk and ProductPage.objects.exists():
            raise ValueError(
                "Only one Product Page can exist."
            )

        super().save(*args, **kwargs)

    
class ProductCategory(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    slug = models.SlugField(
        max_length=100,
        unique=True
    )

    description = models.TextField(
        blank=True
    )

    active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Product Category"
        verbose_name_plural = "Product Categories"

    def __str__(self):
        return self.name


class PartnerProduct(models.Model):
    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        related_name="products"
    )

    category = models.ForeignKey(
        ProductCategory,
        on_delete=models.PROTECT,
        related_name="products"
    )

    name = models.CharField(
        max_length=200
    )

    description = models.TextField(
        blank=True
    )

    image = models.ImageField(
        upload_to="partners/products/",
        blank=True,
        null=True
    )

    product_url = models.URLField(
        blank=True,
        help_text="Optional link to the product on the partner's website."
    )

    active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Partner Product"
        verbose_name_plural = "Partner Products"

    def __str__(self):
        return f"{self.partner.name} - {self.name}"