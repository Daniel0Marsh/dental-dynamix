from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class HomePage(models.Model):
    """
    Singleton content model for the website homepage.

    The number and layout of homepage cards are deliberately fixed.
    This model controls content only: text, images and image alt text.
    """

    # =========================================================
    # HERO
    # =========================================================
    hero_image = models.ImageField(
        upload_to="home/",
        help_text="Upload the hero image for the homepage.",
        default="default/hero_image.webp",
    )

    hero_image_alt_text = models.CharField(
        max_length=255,
        help_text="Provide alternative text for the hero image for accessibility.",
        default="Dental Dynamix Hero Image",
    )

    hero_title = models.TextField(
        help_text="The main title displayed on the homepage hero section.",
        default="Advanced Dental Imaging. Clearer Data. Better Decisions.",
    )

    hero_subtitle = models.TextField(
        help_text="The subtitle displayed below the main title in the hero section.",
        default="Dental Dynamix provides advanced dental imaging solutions that empower dental professionals to make better decisions for their patients.",
    )

    # =========================================================
    # SERVICES SECTION
    # =========================================================

    services_eyebrow = models.CharField(
        max_length=255,
        help_text="Small label displayed above the services heading.",
        default="What we do",
    )

    services_title = models.CharField(
        max_length=255,
        help_text="Main heading for the services section.",
        default="Technology built around your practice",
    )

    services_description = models.TextField(
        help_text="Introductory text displayed beside the services heading.",
        default=(
            "From clinical imaging to the infrastructure behind it, "
            "we help dental practices build technology that works together."
        ),
    )

    #========================================================
    service_card_1_title = models.CharField(
        max_length=255,
        help_text="Title for service card one.",
        default="3D Imaging",
    )

    service_card_1_description = models.TextField(
        help_text="Description for service card one.",
        default="We provide a full turn-key solution when integrating CBCT or OPG technology at your dental practice.",
    )

    service_card_1_image = models.ImageField(
        upload_to="home/",
        help_text="Image displayed in service card one.",
        default="default/service_card_1_image.webp"
    )

    service_card_1_image_alt_text = models.CharField(
        max_length=255,
        help_text="Alternative text for service card one image.",
        default="Dental 3D imaging technology",
    )

    #========================================================

    service_card_2_title = models.CharField(
        max_length=255,
        help_text="Title for service card two.",
        default="2D Imaging",
    )

    service_card_2_description = models.TextField(
        help_text="Description for service card two.",
        default="We know that you want to provide the best diagnosis for your patients, and the best diagnosis starts with the best image quality.",
    )

    service_card_2_image = models.ImageField(
        upload_to="home/",
        help_text="Image displayed in service card two.",
        default="default/service_card_2_image.webp"
    )

    service_card_2_image_alt_text = models.CharField(
        max_length=255,
        help_text="Alternative text for service card two image.",
        default="Dental 2D imaging technology",
    )

    #========================================================

    service_card_3_title = models.CharField(
        max_length=255,
        help_text="Title for service card three.",
        default="IT Support",
    )

    service_card_3_description = models.TextField(
        help_text="Description for service card three.",
        default="We undertake IT support for all our clients using a proactive methodology that utilises the latest technology.",
    )

    service_card_3_image = models.ImageField(
        upload_to="home/",
        help_text="Image displayed in service card three.",
        default="default/service_card_3_image.webp"
    )

    service_card_3_image_alt_text = models.CharField(
        max_length=255,
        help_text="Alternative text for service card three image.",
        default="Dental IT support technology",
    )

    # =========================================================
    # FEATURED PRODUCTS SECTION
    # =========================================================

    featured_products_eyebrow = models.CharField(
        max_length=255,
        help_text="Small label displayed above the featured products heading.",
        default="Featured technology",
    )

    featured_products_title = models.CharField(
        max_length=255,
        help_text="Main heading for the featured products section.",
        default="Products from trusted dental technology partners",
    )

    featured_products_description = models.TextField(
        help_text="Introductory text for the featured products section.",
        default=(
            "Explore selected products and solutions designed for "
            "modern dental practices."
        ),
    )

    featured_products_empty_text = models.CharField(
        max_length=255,
        help_text="Message displayed when there are no featured products.",
        default="Our featured products will be displayed here.",
    )

    # =========================================================
    # IMAGING FEATURE
    # =========================================================

    imaging_eyebrow = models.CharField(
        max_length=255,
        help_text="Small label displayed above the imaging heading.",
        default="Digital dentistry",
    )

    imaging_title = models.CharField(
        max_length=255,
        help_text="Main heading for the digital dentistry section.",
        default="Digital imaging solutions for modern dental practices",
    )

    imaging_description = models.TextField(
        help_text="Introductory text for the digital dentistry section.",
        default=(
            "Dental Dynamix works with leading dental technology manufacturers "
            "to supply and support imaging systems that integrate into modern "
            "clinical workflows."
        ),
    )

    imaging_image = models.ImageField(
        upload_to="home/",
        help_text="Image displayed in the digital dentistry section.",
        default="default/imaging_image.webp",
        blank=True,
    )

    imaging_image_alt_text = models.CharField(
        max_length=255,
        help_text="Alternative text for the digital dentistry image.",
        default="Dental digital imaging technology",
    )


    # =========================================================
    # COMPLETE PRACTICE TECHNOLOGY
    # =========================================================

    practice_technology_eyebrow = models.CharField(
        max_length=255,
        help_text="Small label displayed above the imaging technology heading.",
        default="Complete imaging technology",
    )

    practice_technology_title = models.CharField(
        max_length=255,
        help_text="Main heading for the complete imaging technology section.",
        default="Everything your practice needs for modern imaging.",
    )

    practice_technology_description = models.TextField(
        help_text="Description for the complete imaging technology section.",
        default=(
            "From 2D digital imaging and intraoral X-ray to CBCT, 3D imaging "
            "and intraoral scanning, we provide the technology and expertise "
            "to help your practice capture, manage and use high-quality "
            "diagnostic images."
        ),
    )

    # =========================================================

    practice_technology_card_1_icon = models.CharField(
        max_length=255,
        help_text="Icon for imaging technology card one.",
        default="bi-boxes",
    )

    practice_technology_card_1_title = models.CharField(
        max_length=255,
        help_text="Title for imaging technology card one.",
        default="CBCT & 3D Imaging",
    )

    practice_technology_card_1_description = models.TextField(
        help_text="Description for imaging technology card one.",
        default=(
            "Advanced CBCT and 3D imaging systems for detailed "
            "diagnostic information and treatment planning."
        ),
    )

    # =========================================================

    practice_technology_card_2_icon = models.CharField(
        max_length=255,
        help_text="Icon for imaging technology card two.",
        default="bi-image",
    )

    practice_technology_card_2_title = models.CharField(
        max_length=255,
        help_text="Title for imaging technology card two.",
        default="2D Digital Imaging",
    )

    practice_technology_card_2_description = models.TextField(
        help_text="Description for imaging technology card two.",
        default=(
            "High-quality digital panoramic and cephalometric imaging "
            "for everyday clinical diagnosis."
        ),
    )

    # =========================================================

    practice_technology_card_3_icon = models.CharField(
        max_length=255,
        help_text="Icon for imaging technology card three.",
        default="bi-camera",
    )

    practice_technology_card_3_title = models.CharField(
        max_length=255,
        help_text="Title for imaging technology card three.",
        default="Intraoral X-Ray",
    )

    practice_technology_card_3_description = models.TextField(
        help_text="Description for imaging technology card three.",
        default=(
            "Digital intraoral X-ray solutions designed for fast, "
            "clear and efficient clinical imaging."
        ),
    )

    # =========================================================

    practice_technology_card_4_icon = models.CharField(
        max_length=255,
        help_text="Icon for imaging technology card four.",
        default="bi-grid-3x3-gap",
    )

    practice_technology_card_4_title = models.CharField(
        max_length=255,
        help_text="Title for imaging technology card four.",
        default="Intraoral Scanning",
    )

    practice_technology_card_4_description = models.TextField(
        help_text="Description for imaging technology card four.",
        default=(
            "Digital intraoral scanning technology for accurate "
            "3D impressions, workflows and patient communication."
        ),
    )

    # =========================================================

    practice_technology_card_5_icon = models.CharField(
        max_length=255,
        help_text="Icon for imaging technology card five.",
        default="bi-window-stack",
    )

    practice_technology_card_5_title = models.CharField(
        max_length=255,
        help_text="Title for imaging technology card five.",
        default="Imaging Software",
    )

    practice_technology_card_5_description = models.TextField(
        help_text="Description for imaging technology card five.",
        default=(
            "Imaging software that helps clinicians view, manage and "
            "work with diagnostic images efficiently."
        ),
    )

    # =========================================================

    practice_technology_card_6_icon = models.CharField(
        max_length=255,
        help_text="Icon for imaging technology card six.",
        default="bi-tools",
    )

    practice_technology_card_6_title = models.CharField(
        max_length=255,
        help_text="Title for imaging technology card six.",
        default="Imaging Integration & Support",
    )

    practice_technology_card_6_description = models.TextField(
        help_text="Description for imaging technology card six.",
        default=(
            "Installation, integration and ongoing technical support "
            "to keep your imaging technology working reliably."
        ),
    )
    # =========================================================
    # COMPLETE SOLUTION
    # =========================================================

    complete_solution_eyebrow = models.CharField(
        max_length=255,
        help_text="Small label displayed above the complete solution heading.",
        default="One technology partner",
    )

    complete_solution_title = models.CharField(
        max_length=255,
        help_text="Main heading for the complete solution section.",
        default="From the network socket to the X-ray image.",
    )

    complete_solution_description = models.TextField(
        help_text="Description for the complete solution section.",
        default=(
            "Dental Dynamix can support the complete technology journey "
            "of your practice — from the PC at reception, through your "
            "network and servers, to imaging equipment and the software "
            "your clinicians use every day."
        ),
    )

    #========================================================

    complete_solution_card_1_icon = models.CharField(
        max_length=255,
        help_text="Icon for complete solution card one.",
        default="bi-pc-display",
    )

    complete_solution_card_1_title = models.CharField(
        max_length=255,
        help_text="Title for complete solution card one.",
        default="Hardware",
    )

    #========================================================

    complete_solution_card_2_icon = models.CharField(
        max_length=255,
        help_text="Icon for complete solution card two.",
        default="bi-wifi",
    )

    complete_solution_card_2_title = models.CharField(
        max_length=255,
        help_text="Title for complete solution card two.",
        default="Networks",
    )

    #========================================================

    complete_solution_card_3_icon = models.CharField(
        max_length=255,
        help_text="Icon for complete solution card three.",
        default="bi bi-camera",
    )

    complete_solution_card_3_title = models.CharField(
        max_length=255,
        help_text="Title for complete solution card three.",
        default="Imaging",
    )

    #========================================================

    complete_solution_card_4_icon = models.CharField(
        max_length=255,
        help_text="Icon for complete solution card four.",
        default="bi bi-headset",
    )

    complete_solution_card_4_title = models.CharField(
        max_length=255,
        help_text="Title for complete solution card four.",
        default="Support",
    )

    # =========================================================
    # PARTNERS SECTION
    # =========================================================

    partners_eyebrow = models.CharField(
        max_length=255,
        help_text="Small label displayed above the partners heading.",
        default="Technology partners",
    )

    partners_title = models.CharField(
        max_length=255,
        help_text="Main heading for the technology partners section.",
        default="Technology you can trust",
    )

    partners_description = models.TextField(
        help_text="Introductory text for the technology partners section.",
        default=(
            "We work with leading dental technology manufacturers "
            "to provide proven products and imaging solutions."
        ),
    )

    partners_empty_text = models.CharField(
        max_length=255,
        help_text="Message displayed when there are no technology partners.",
        default="Our technology partners will be displayed here.",
    )

    # =========================================================
    # FINAL CTA
    # =========================================================

    final_cta_eyebrow = models.CharField(
        max_length=255,
        help_text="Small label displayed above the final CTA heading.",
        default="Let's talk",
    )

    final_cta_title = models.CharField(
        max_length=255,
        help_text="Main heading for the final CTA section.",
        default="Planning a new practice, upgrade or imaging project?",
    )

    final_cta_description = models.TextField(
        help_text="Description displayed in the final CTA section.",
        default=(
            "Tell us what you're looking to achieve and we'll "
            "help you find the right technology solution."
        ),
    )





    # =========================================================
    # ADMIN / META
    # =========================================================

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Automatically updated whenever the homepage content changes.",
    )

    class Meta:
        verbose_name = "Homepage"
        verbose_name_plural = "Homepage"

    def __str__(self):
        return "Homepage"

    def save(self, *args, **kwargs):
        """
        Ensure that only one homepage record exists.
        """
        self.pk = 1
        super().save(*args, **kwargs)


class TermsAndConditionsPage(models.Model):
    """
    Model representing the terms and conditions page.
    """

    title = models.CharField(
        max_length=200,
        default="Terms and Conditions",
    )

    content = CKEditor5Field(
        config_name='default',
        default=(
            "Please view or download our Terms and Conditions below. "
            "This document contains the terms and conditions that apply "
            "to our services."
        ),
        blank=True,
    )

    pdf = models.FileField(
        upload_to='terms-and-conditions/',
        help_text="Upload the PDF file for the terms and conditions.",
        default="default/Dental_Dynamix_Terms_and_Conditions.pdf",
    )

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Terms and Conditions Page"
        verbose_name_plural = "Terms and Conditions Page"     