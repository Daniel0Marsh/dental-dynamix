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


class PartnerProduct(models.Model):

    CATEGORY_CHOICES = (
        ("cbcts", "CBCTs"),
        ("opgs", "OPGs"),
        ("ios", "Intraoral 3D Scanners (IOS)"),
        ("phosphor_plate_scanners", "Phosphor Plate Scanners"),
        ("intraoral_2d_sensors", "Intraoral 2D Sensors"),
        ("intraoral_xray_generators", "Intraoral X-Ray Generators"),
        ("software", "Software"),
    )

    partner = models.ForeignKey(
        Partner,
        on_delete=models.CASCADE,
        related_name="products"
    )

    category = models.CharField(
        max_length=40,
        choices=CATEGORY_CHOICES
    )

    name = models.CharField(
        max_length=200
    )

    slug = models.SlugField(
        max_length=200,
        blank=True,
        null=True,
    )

    description = models.TextField(
        blank=True,
        help_text=(
            "Short product description used on product listings "
            "and the homepage."
        )
    )

    detailed_description = models.TextField(
        blank=True,
        help_text=(
            "Detailed product description displayed on the "
            "product detail page."
        )
    )

    features = models.TextField(
        blank=True,
        help_text=(
            "Key product features. Add one feature per line."
        )
    )

    image = models.ImageField(
        upload_to="partners/products/",
        blank=True,
        null=True,
        help_text=(
            "Main product image. This image is also used when "
            "the product is featured on the homepage."
        )
    )

    product_url = models.URLField(
        blank=True,
        help_text=(
            "Optional link to the product on the partner's website."
        )
    )

    active = models.BooleanField(
        default=True
    )

    show_on_homepage = models.BooleanField(
        default=False,
        help_text=(
            "Show this product in the featured products section "
            "on the homepage."
        )
    )

    homepage_order = models.PositiveIntegerField(
        default=0,
        help_text=(
            "Controls the order of this product in the homepage "
            "featured products section."
        )
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Partner Product"
        verbose_name_plural = "Partner Products"
        constraints = [
            models.UniqueConstraint(
                fields=["partner", "slug"],
                name="unique_product_slug_per_partner",
            ),
        ]

    def __str__(self):
        return f"{self.partner.name} - {self.name}"

    def get_absolute_url(self):
        return reverse(
            "partners:product_detail",
            kwargs={
                "partner_slug": self.partner.slug,
                "slug": self.slug,
            },
        )


class PartnerProductImage(models.Model):
    product = models.ForeignKey(
        PartnerProduct,
        on_delete=models.CASCADE,
        related_name="gallery_images"
    )

    image = models.ImageField(
        upload_to="partners/products/gallery/",
        help_text="Additional product image."
    )

    alt_text = models.CharField(
        max_length=255,
        blank=True,
        help_text=(
            "Alternative text for accessibility and SEO."
        )
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "id"]
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"

    def __str__(self):
        return f"{self.product.name} - Image {self.pk}"


class PartnerProductDocument(models.Model):

    DOCUMENT_TYPES = (
        ("manual", "User Manual"),
        ("installation", "Installation Guide"),
        ("technical", "Technical Manual"),
        ("datasheet", "Datasheet"),
        ("brochure", "Brochure"),
        ("other", "Other"),
    )

    product = models.ForeignKey(
        PartnerProduct,
        on_delete=models.CASCADE,
        related_name="documents"
    )

    title = models.CharField(
        max_length=200
    )

    document_type = models.CharField(
        max_length=20,
        choices=DOCUMENT_TYPES,
        default="manual"
    )

    file = models.FileField(
        upload_to="partners/products/documents/",
        help_text=(
            "Upload the product document. PDF is recommended."
        )
    )

    active = models.BooleanField(
        default=True
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "title"]
        verbose_name = "Product Document"
        verbose_name_plural = "Product Documents"

    def __str__(self):
        return f"{self.product.name} - {self.title}"


class PartnerProductSpecification(models.Model):

    product = models.ForeignKey(
        PartnerProduct,
        on_delete=models.CASCADE,
        related_name="specifications"
    )

    name = models.CharField(
        max_length=200
    )

    value = models.CharField(
        max_length=500
    )

    display_order = models.PositiveIntegerField(
        default=0
    )

    class Meta:
        ordering = ["display_order", "name"]
        verbose_name = "Product Specification"
        verbose_name_plural = "Product Specifications"

    def __str__(self):
        return f"{self.product.name} - {self.name}"