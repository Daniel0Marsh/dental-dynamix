from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class AboutPage(models.Model):
    """
    Singleton model for the About Us page content.
    """

    # =========================================================
    # Hero Section
    # =========================================================

    hero_image = models.ImageField(
        upload_to="about/",
        default="default/hero_image.webp",
        blank=True,
        help_text=(
            "Main hero image displayed at the top of the About page."
        ),
    )

    hero_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Dental Dynamix dental technology and equipment supplier "
            "providing digital dentistry and imaging solutions"
        ),
        help_text=(
            "Alternative text for the hero image for SEO "
            "and accessibility."
        ),
    )

    hero_title = models.CharField(
        max_length=200,
        default="Your Dental Technology Partner",
        blank=True,
        help_text=(
            "Primary headline shown in the hero section."
        ),
    )

    hero_subtitle = models.CharField(
        max_length=300,
        default=(
            "Dental Dynamix provides dental practices with the technology, "
            "equipment, imaging solutions and technical support they need "
            "to work smarter and deliver exceptional patient care."
        ),
        blank=True,
        help_text=(
            "Short supporting text displayed beneath the hero title."
        ),
    )


    # =========================================================
    # Mission Section
    # =========================================================

    mission_image = models.ImageField(
        upload_to="about/",
        default="default/our_mission_image.webp",
        blank=True,
        help_text=(
            "Image displayed alongside the mission statement."
        ),
    )

    mission_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Dental Dynamix providing dental technology, equipment, "
            "IT support and digital imaging solutions"
        ),
        help_text=(
            "Alternative text for the mission image for SEO "
            "and accessibility."
        ),
    )

    mission_title = models.CharField(
        max_length=200,
        default="Our Mission",
        blank=True,
        help_text=(
            "Heading for the mission section."
        ),
    )

    mission_text = CKEditor5Field(
        default=(
            "<p>At Dental Dynamix, our mission is simple: to provide dental "
            "practices with the technology, equipment and support they need "
            "to operate efficiently and deliver the highest standard of "
            "patient care.</p>"

            "<p>We work across the dental technology landscape, from IT "
            "infrastructure and technical support to advanced 2D and 3D "
            "digital imaging solutions. By combining practical technical "
            "expertise with high-quality products from leading manufacturers, "
            "we help dental professionals make confident decisions about "
            "the technology they rely on every day.</p>"

            "<p>We work closely with trusted industry partners, including "
            "Planmeca, DEXIS and other leading dental technology manufacturers, "
            "allowing us to provide practices with reliable solutions "
            "tailored to their individual requirements.</p>"
        ),
        blank=True,
        help_text=(
            "Main text describing Dental Dynamix's mission and purpose."
        ),
    )


    # =========================================================
    # Technology & Support Section
    # =========================================================

    values_image = models.ImageField(
        upload_to="about/",
        default="default/our_values_image.webp",
        blank=True,
        help_text=(
            "Image representing Dental Dynamix's technology, "
            "services or support capabilities."
        ),
    )

    values_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Dental Dynamix team delivering reliable dental technology "
            "and digital imaging solutions"
        ),
        help_text=(
            "Alternative text for the technology and support image "
            "for SEO and accessibility."
        ),
    )

    values_title = models.CharField(
        max_length=200,
        default="Technology That Works for Your Practice",
        blank=True,
        help_text=(
            "Heading for the technology and support section."
        ),
    )

    values_text = CKEditor5Field(
        default=(
            "<p>At Dental Dynamix, we believe that technology should make "
            "running a dental practice easier, not more complicated.</p>"

            "<p>We focus on providing dependable products, practical advice "
            "and responsive technical support. Whether a practice needs "
            "help with its IT infrastructure, is considering a new imaging "
            "system or is looking to improve its digital workflow, we take "
            "the time to understand what is actually required.</p>"

            "<p>Our approach is built around quality, reliability and "
            "long-term relationships. We work with established manufacturers "
            "and technology partners to provide solutions that we can stand "
            "behind, while maintaining the hands-on support our customers "
            "expect from a specialist dental technology supplier.</p>"

            "<p>From everyday IT support to advanced 2D and 3D imaging "
            "technology, our goal is to help dental practices get the most "
            "from their technology.</p>"
        ),
        blank=True,
        help_text=(
            "Description of Dental Dynamix's technology, services "
            "and support approach."
        ),
    )


    # =========================================================
    # Why Dental Dynamix Section
    # =========================================================

    team_image = models.ImageField(
        upload_to="about/",
        default="default/our_team_image.webp",
        blank=True,
        help_text=(
            "Image representing Dental Dynamix, its team or "
            "its approach to supporting dental practices."
        ),
    )

    team_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Dental Dynamix team supporting dental practices "
            "with technology and imaging solutions"
        ),
        help_text=(
            "Alternative text for the Why Dental Dynamix image "
            "for SEO and accessibility."
        ),
    )

    team_title = models.CharField(
        max_length=200,
        default="Why Dental Dynamix?",
        blank=True,
        help_text=(
            "Heading for the section explaining the Dental Dynamix "
            "approach and expertise."
        ),
    )

    team_text = CKEditor5Field(
        default=(
            "<p>Dental Dynamix brings together experience across dental "
            "technology, IT and digital imaging to provide practices with "
            "a single point of support for their technology needs.</p>"

            "<p>We understand that every dental practice is different. "
            "That is why we take a practical, consultative approach, "
            "working with our customers to understand their existing "
            "systems, their workflow and where technology can make a "
            "genuine difference.</p>"

            "<p>Our relationships with leading manufacturers and technology "
            "partners, including Planmeca and DEXIS, allow us to offer "
            "access to established dental technology while providing the "
            "independent guidance and technical support needed to get the "
            "most from it.</p>"

            "<p>Whether you are setting up a new practice, upgrading your "
            "existing equipment or simply need reliable IT support, "
            "Dental Dynamix is here to help.</p>"
        ),
        blank=True,
        help_text=(
            "Description of the Dental Dynamix approach, expertise "
            "and customer support."
        ),
    )


    # =========================================================
    # Meta
    # =========================================================

    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    def __str__(self):
        return "About Page"


class Testimonial(models.Model):
    """
    Represents a single testimonial displayed on the website.
    """

    quote = models.TextField(
        default="This is an amazing service! Highly recommended.",
        help_text=(
            "The testimonial text shown in the quote card."
        ),
    )

    author_name = models.CharField(
        max_length=100,
        default="Daniel Marsh",
        help_text=(
            "Name of the person giving the testimonial."
        ),
    )

    author_company = models.CharField(
        max_length=100,
        blank=True,
        default="Dental Dynamix",
        help_text=(
            "Optional company or organisation associated with the testimonial."
        ),
    )

    is_active = models.BooleanField(
        default=True,
        help_text=(
            "Only active testimonials will be shown on the website."
        ),
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text=(
            "Controls the order testimonials appear in. "
            "Lower numbers appear first."
        ),
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text=(
            "Date this testimonial was created."
        ),
    )

    class Meta:
        ordering = ["display_order", "created_at"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self) -> str:
        return f"{self.author_name} – Testimonial"