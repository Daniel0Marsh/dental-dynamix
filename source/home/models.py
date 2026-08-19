from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class HomePage(models.Model):
    """
    Model representing the homepage information for the website.
    Includes hero section, service cards, and about section.
    """

    hero_image = models.FileField(
        upload_to="home_page/images/",
        help_text="Upload the hero section image.",
        default="default/hero_image.webp"
    )

    hero_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Advanced dental imaging technology and digital solutions "
            "from Dental Dynamix"
        ),
        help_text=(
            "Provide alternative text for the hero image for SEO "
            "and accessibility purposes."
        )
    )

    hero_subtitle = models.CharField(
        max_length=255,
        help_text="Subtitle text for the hero section.",
        default=(
            "Industry-leading 2D and 3D dental imaging solutions "
            "designed to improve diagnostic accuracy, workflow "
            "efficiency, and patient outcomes."
        )
    )

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    # --- Service Cards Section ---
    service_card_1_title = models.CharField(
        max_length=100,
        default="3D Imaging",
        help_text="Title for Service Card 1"
    )
    service_card_1_description = models.TextField(
        default="We provide a full turn-key solution when integrating CBCT or OPG technology at your dental practice.",
        help_text="Description for Service Card 1"
    )
    service_card_1_image = models.ImageField(
        upload_to="service_cards/",
        default="default/service_card_1_image.webp",
        help_text="Background image for Service Card 1"
    )

    service_card_2_title = models.CharField(
        max_length=100,
        default="2D Imaging",
        help_text="Title for Service Card 2"
    )
    service_card_2_description = models.TextField(
        default="We know that you want to provide the best diagnosis for your patients, and the best diagnosis starts with the best image quality.",
        help_text="Description for Service Card 2"
    )
    service_card_2_image = models.ImageField(
        upload_to="service_cards/",
        default="default/service_card_2_image.webp",
        help_text="Background image for Service Card 2"
    )

    service_card_3_title = models.CharField(
        max_length=100,
        default="IT Support",
        help_text="Title for Service Card 3"
    )
    service_card_3_description = models.TextField(
        default="We undertake IT support for all our clients using a proactive methodology that utilises the latest technology. ",
        help_text="Description for Service Card 3"
    )
    service_card_3_image = models.ImageField(
        upload_to="service_cards/",
        default="default/service_card_3_image.webp",
        help_text="Background image for Service Card 3"
    )

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------


    # --- About Section ---
    about_image = models.FileField(
        upload_to="home_page/images/",
        help_text="Upload the image for the About section.",
        default="default/about_image.webp"
    )
    about_image_alt_text = models.CharField(
        max_length=255, 
        default="Dental Dynamix is a Kent-based web design agency specialising CBCT and OPG imaging solutions for dental practices, providing expert support and innovative technology to enhance patient care.", 
        help_text="Provide alternative text for the image for SEO and accessibility purposes."
    )
    about_title = models.CharField(
        max_length=255,
        default="About Dental Dynamix",
        help_text="Title text for the About section."
    )

    about_copy = models.TextField(
        default="At Dental Dynamix, we are committed to providing dental practices with innovative technology, expert support, and reliable solutions that help improve patient care and practice efficiency.",
        help_text="Copy text for the About section."
    )
    about_url = models.URLField(
        default="https://dentaldynamix.co.uk",
        help_text="Button URL for the About section"
    )


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------

    # --- Testimonial Section ---
    testimonial_image = models.FileField(
        upload_to="home_page/testimonials/",
        default="default/testimonial_bg.webp",
        help_text=(
            "Background image for the testimonial section. "
        )
    )
    testimonial_image_alt_text = models.CharField(
        max_length=255, 
        default="Satisfied dental practice owners sharing their experience with Dental Dynamix's imaging solutions", 
        help_text="Provide alternative text for the image for SEO and accessibility purposes."
    )


    #-----------------------------------------------------------------------------------------------------------------------------------------------------------------


    # --- Support Section ---
    support_image = models.FileField(
        upload_to="home_page/images/",
        help_text="Upload the image for the Support section.",
        default="default/support_image.webp"
    )
    support_image_alt_text = models.CharField(
        max_length=255, 
        default="Kent-based web design agency specialising in custom websites, UI/UX design, and business growth", 
        help_text="Provide alternative text for the image for SEO and accessibility purposes."
    )
    support_title = models.CharField(
        max_length=255,
        default="Reliable Dental IT Support Built for Modern Practices",
        help_text="Title text for the Support section."
    )
    support_copy = models.TextField(
        default="Dental practices depend on stable, secure, and compliant technology. Dental Dynamix delivers specialist IT support designed specifically for the demands of digital dentistry — ensuring your systems run smoothly, securely, and without disruption. From day-to-day troubleshooting to full infrastructure management, we keep your practice connected, protected, and productive.",
        help_text="Copy text for the Support section."
    )
    support_url = models.URLField(
        default="https://dentaldynamix.co.uk",
        help_text="Button URL for the Support section"
    )

    def __str__(self) -> str:
        return "Home Page Info"

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Page"


class PrivacyPolicyPage(models.Model):
    """
    Model representing the privacy policy.
    """
    content = CKEditor5Field(config_name='default', null=True, blank=True)

    def __str__(self) -> str:
        return "Privacy Policy"

    class Meta:
        verbose_name = "Privacy Policy Page"
        verbose_name_plural = "Privacy Policy Page"
        