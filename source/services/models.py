from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class ServicePage(models.Model):
    SERVICE_CHOICES = [
        ("web-design", "Web Design"),
        ("wordpress-django", "WordPress / Django"),
        ("hosting-maintenance", "Hosting & Maintenance"),
        ("seo-marketing", "SEO & Marketing"),
    ]

    service = models.CharField(
        max_length=50,
        choices=SERVICE_CHOICES,
        unique=True
    )

    # -----------------
    # Timestamps
    # -----------------
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="The date and time when the page was last updated."
    )


    # -----------------
    # Hero Section
    # -----------------
    hero_image = models.ImageField(
        upload_to="Service/",
        default="default/service_hero_image.webp",
        blank=True
    )
    hero_image_alt_text = models.CharField(
        max_length=255, 
        default="Award-winning web design agency in Kent, UK delivering custom websites for local businesses", 
        help_text="Provide alternative text for the image for SEO and accessibility purposes."
    )
    hero_title = models.CharField(
        max_length=200,
        default="Professional Web Development Services"
    )
    hero_subtitle = models.CharField(
        max_length=300,
        blank=True,
        default="We build modern, responsive, and scalable websites tailored to your business needs."
    )

    # -----------------
    # Info Section
    # -----------------
    info_image = models.ImageField(
        upload_to="Service/",
        default="default/service_info_image.webp",
        blank=True
    )
    info_image_alt_text = models.CharField(
        max_length=255, 
        default="Kent-based web design agency specialising in custom websites, UI/UX design, and business growth", 
        help_text="Provide alternative text for the image for SEO and accessibility purposes."
    )
    info_title = models.CharField(
        max_length=200,
        default="Why Choose Our Services?"
    )
    info_text = CKEditor5Field(
        blank=True,
        default=(
            "Our team specialises in delivering high-quality websites with exceptional user experience, "
            "robust backend architecture, and seamless integrations. "
            "We work closely with our clients to understand their goals and provide tailored solutions "
            "that drive engagement and growth."
        )
    )

    # -----------------
    # Support Section
    # -----------------
    support_image = models.ImageField(
        upload_to="Service/",
        default="default/service_support_image.webp",
        blank=True
    )
    support_image_alt_text = models.CharField(
        max_length=255, 
        default="Kent-based web design agency building modern, fast, and user-friendly websites for businesses", 
        help_text="Provide alternative text for the image for SEO and accessibility purposes."
    )
    support_title = models.CharField(
        max_length=200,
        default="We Support You"
    )
    support_text = CKEditor5Field(
        blank=True,
        default=(
            "Our support team is available to assist you at every stage, from deployment to maintenance, "
            "ensuring your website runs smoothly. "
            "We provide ongoing guidance, updates, and troubleshooting, so you can focus on your business "
            "while we take care of the technical details."
        )
    )

    # -----------------
    # Pricing Section
    # -----------------
    pricing_1_title = models.CharField(
        max_length=200,
        default="Basic Plan"
    )
    pricing_1_amount = models.CharField(
        max_length=50,
        default="£499"
    )
    pricing_1_support_text = models.CharField(
        max_length=100,
        default="Includes basic website setup and support."
    )

    pricing_2_title = models.CharField(
        max_length=200,
        default="Premium Plan"
    )
    pricing_2_amount = models.CharField(
        max_length=50,
        default="£999"
    )
    pricing_2_support_text = models.CharField(
        max_length=100,
        default="Includes full website development, SEO optimisation, and premium support."
    )

    class Meta:
        verbose_name = "Service Page"
        verbose_name_plural = "Service Pages"

    def __str__(self):
        return self.get_service_display()
