from django.db import models

class Branding(models.Model):
    """
    Model representing the Branding information for the website.

    Stores company branding, contact info, media assets, working hours,
    SEO fields, and social media links for structured data.
    """

    under_construction = models.BooleanField(
        default=False,
        help_text="Enable the under-construction overlay and disable website interaction."
    )

    company_name = models.CharField(
        max_length=255,
        help_text="Full company name",
        default="Dental Dynamix"
    )
    company_email = models.EmailField(
        help_text="Official company email",
        default="support@dentaldynamix.co.uk"
    )
    company_phone = models.CharField(
        max_length=20,
        help_text="Company contact number",
        default="01622 585675"
    )
    company_address = models.CharField(
        max_length=255,
        help_text="Full address, including city and ZIP",
        default="Kent, UK"
    )
    working_hours = models.CharField(
        max_length=255,
        help_text="Working hours (for local SEO)",
        default="Mon - Fri: 09:00 - 18:00"
    )
    top_bar = models.CharField(
        max_length=255,
        help_text="Top bar text",
        default="Call Us Today: 01622 585675"
    )

    # Logos
    logo = models.ImageField(upload_to="branding/", default="default/logo.svg")
    logo_alt_text = models.CharField(max_length=255, default="Dental Dynamix logo – Web Development Agency")
    logo_geo_tag = models.CharField(max_length=255, blank=True, default="51.2787,1.0810")
    favicon = models.ImageField(upload_to="branding/", default="default/favicon.ico")

    # SEO
    site_map_description = models.TextField(
        blank=True,
        default=(
            "Dental Dynamix is a leading provider of dental imaging solutions, including CBCT, X-ray, and 3D imaging. "
        )
    )
    meta_keywords = models.CharField(
        max_length=512,
        blank=True,
        default="Dental Dynamix, CBCT, Xray, 3D Imaging, Dental Software, Planmecca, DEXIS, Carestream, Sirona, Dental Imaging, Dental Technology, Dental Solutions, Dental Services"
    )

    # Social media links (for structured data / JSON-LD)
    facebook_url = models.URLField(blank=True, default="https://www.facebook.com/dentaldynamix")
    twitter_url = models.URLField(blank=True, default="https://twitter.com/dentaldynamix")
    linkedin_url = models.URLField(blank=True, default="https://www.linkedin.com/company/dentaldynamix")
    instagram_url = models.URLField(blank=True, default="https://www.instagram.com/dentaldynamix")

    def social_links(self):
        """Return all non-empty social links as a list for JSON-LD"""
        links = []
        for url in [self.facebook_url, self.twitter_url, self.linkedin_url, self.instagram_url]:
            if url:
                links.append(url)
        return links

    def __str__(self):
        return "Branding Info"

    class Meta:
        verbose_name = "Branding"
        verbose_name_plural = "Branding"
