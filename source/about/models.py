from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

from django.db import models


class AboutPage(models.Model):
    """
    Singleton model for the About Us page content.
    """

    # -----------------
    # Hero Section
    # -----------------
    hero_image = models.ImageField(
        upload_to="about/",
        default="default/hero_image.webp",
        blank=True,
        help_text="Main hero image displayed at the top of the About page."
    )

    hero_image_alt_text = models.CharField(
        max_length=255, 
        default="Award-winning web design agency in Kent, UK delivering custom websites for local businesses", 
        help_text="Provide alternative text for the image for SEO and accessibility purposes."
    )

    hero_title = models.CharField(
        max_length=200,
        default="About Our Web Design and Hosting Agency",
        blank=True,
        help_text="Primary headline shown in the hero section."
    )
    hero_subtitle = models.CharField(
        max_length=300,
        default="We are a UK-based website design and hosting agency supporting businesses across Kent with reliable, well-crafted digital solutions built for long-term success.",
        blank=True,
        help_text="Short supporting text displayed beneath the hero title."
    )

    # -----------------
    # Mission Section
    # -----------------
    mission_image = models.ImageField(
        upload_to="about/",
        default="default/our_mission_image.webp",
        blank=True,
        help_text="Image displayed alongside the mission statement."
    )
    mission_image_alt_text = models.CharField(
        max_length=255, 
        default="Kent-based web design agency specialising in custom websites, UI/UX design, and business growth", 
        help_text="Provide alternative text for the image for SEO and accessibility purposes."
    )
    mission_title = models.CharField(
        max_length=200,
        default="Our Mission",
        blank=True,
        help_text="Heading for the mission section."
    )
    mission_text = CKEditor5Field(
        default=(
            "<p>Our mission is to help businesses across Kent and the UK succeed online with technically "
            "sound, reliable, and easy-to-maintain websites.</p>"
            "<p>We combine thoughtful design, robust development, and dependable hosting to deliver "
            " digital solutions that support growth and build customer trust.</p>"
        ),
        blank=True,
        help_text="Main text describing the company’s mission and purpose."
    )

    # -----------------
    # Values Section
    # -----------------
    values_image = models.ImageField(
        upload_to="about/",
        default="default/our_values_image.webp",
        blank=True,
        help_text="Image representing the company’s values."
    )
    values_image_alt_text = models.CharField(
        max_length=255, 
        default="Kent-based web design agency building modern, fast, and user-friendly websites for businesses", 
        help_text="Provide alternative text for the image for SEO and accessibility purposes."
    )
    values_title = models.CharField(
        max_length=200,
        default="Our Values",
        blank=True,
        help_text="Heading for the values section."
    )
    values_text = CKEditor5Field(
        default=(
            "<p>Our work is guided by a strong commitment to quality, transparency, and long-term relationships.</p>"
            "<p>We value clear communication, realistic expectations, and well-engineered solutions that prioritise "
            "performance, security, and usability from the outset.</p>"
            "<p>As a Kent-based website design and hosting agency, we take pride in offering a personal and dependable "
            "service. We focus on doing things properly, building websites that are maintainable, search-engine friendly, "
            "and supported by reliable hosting so our clients can feel confident in their digital foundations.</p>"
        ),
        blank=True,
        help_text="Description of the core values that guide the company."
    )

    # -----------------
    # Our Team Section
    # -----------------
    team_image = models.ImageField(
        upload_to="about/",
        default="default/our_team_image.webp",
        blank=True,
        help_text="Image representing the team or company culture."
    )
    team_image_alt_text = models.CharField(
        max_length=255, 
        default="Experienced web designers in Kent, UK working on modern, user-focused business websites", 
        help_text="Provide alternative text for the image for SEO and accessibility purposes."
    )
    team_title = models.CharField(
        max_length=200,
        default="Our Team",
        blank=True,
        help_text="Heading for the team section."
    )
    team_text = CKEditor5Field(
        default=(
            "<p>We are a small, focused team of web developers and designers based in the UK, working closely "
            "with businesses throughout Kent and the surrounding areas.</p>"
            "<p>Our size allows us to remain agile, detail-oriented, and directly involved in every project we take on.</p>"
            "<p>Rather than outsourcing or taking a one-size-fits-all approach, we work hands-on with our clients to "
            "understand their business, their goals, and their challenges.</p>"
        ),
        blank=True,
        help_text="Description of the team and how they work together."
    )


    class Meta:
        verbose_name = "About Page"
        verbose_name_plural = "About Page"

    def __str__(self):
        return "About Page"




class Testimonial(models.Model):
    """
    Represents a single testimonial displayed on the homepage.
    """

    quote = models.TextField(
        default="This is an amazing service! Highly recommended.",
        help_text="The testimonial text shown in the quote card."
    )

    author_name = models.CharField(
        max_length=100,
        default="Daniel Marsh",
        help_text="Name of the person giving the testimonial."
    )

    author_company = models.CharField(
        max_length=100,
        blank=True,
        default="Dental Dynamix",
        help_text="Optional company name (e.g. Tech Solutions Inc.)."
    )

    is_active = models.BooleanField(
        default=True,
        help_text="Only active testimonials will be shown on the website."
    )

    display_order = models.PositiveIntegerField(
        default=0,
        help_text="Controls the order testimonials appear (lower = first)."
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="Date this testimonial was created."
    )

    class Meta:
        ordering = ["display_order", "created_at"]
        verbose_name = "Testimonial"
        verbose_name_plural = "Testimonials"

    def __str__(self) -> str:
        return f"{self.author_name} – Testimonial"

