from django.db import models
from django.urls import reverse


class ITSupportPage(models.Model):

    # Hero
    hero_image = models.ImageField(
        upload_to="it-support/",
        default="default/hero_image.webp",
        help_text=(
            "Wide background image for the hero section. "
            "Choose an image relevant to practice IT, with space "
            "for the heading on the left. Uses the existing default "
            "hero image until replaced."
        ),
    )
    hero_image_alt_text = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text=(
            "Briefly describe the uploaded image if it conveys useful "
            "information. Leave empty if it is purely decorative."
        ),
    )
    hero_title = models.CharField(
        max_length=255,
        default="IT Support for Your Dental Practice",
        help_text="Main page heading displayed over the hero image.",
    )
    hero_subtitle = models.TextField(
        default=(
            "From day-to-day IT questions to protection and backup "
            "requirements, talk to Dental Dynamix about the technology "
            "your practice depends on."
        ),
        help_text=(
            "Short introduction beneath the main heading. "
            "Summarise the page without promising response times "
            "or services that have not been confirmed."
        ),
    )
    hero_primary_button_text = models.CharField(
        max_length=100,
        default="Discuss Your IT Requirements",
        help_text=(
            "Label for the hero button. "
            "The button links to the Contact page."
        ),
    )

    # Overview
    overview_eyebrow = models.CharField(
        max_length=100,
        default="How We Can Help",
        help_text="Small introductory label above the overview heading.",
    )
    overview_heading = models.CharField(
        max_length=200,
        default="IT Support, IT Protect and Backup",
        help_text="Heading introducing the three service cards.",
    )
    overview_description = models.TextField(
        default=(
            "Every practice has different systems and priorities. "
            "Tell us about your current setup, the challenges you "
            "are facing and what you would like to improve. "
            "We can discuss your support, protection and backup "
            "requirements and the appropriate next steps."
        ),
        help_text=(
            "Introduction above the cards. Explain how visitors "
            "can begin a discussion about their practice IT."
        ),
    )

    # IT Support
    support_title = models.CharField(
        max_length=150,
        default="IT Support",
        help_text="Heading for the first service card.",
    )
    support_description = models.TextField(
        default=(
            "Having trouble with a practice computer, network "
            "connection or software setup? Describe the issue "
            "and the systems involved so we can discuss the "
            "support you need and how best to proceed."
        ),
        help_text=(
            "Description of IT Support. Confirm the supported systems, "
            "service scope and any support arrangements with Dmitry. "
            "Paragraph breaks are supported."
        ),
    )
    support_image = models.ImageField(
        upload_to="it-support/",
        blank=True,
        help_text=(
            "Optional image for the IT Support card. "
            "Use a landscape image suited to a 16:9 crop. "
            "Leave empty to show the card without an image."
        ),
    )
    support_image_alt = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text=(
            "Describe the IT Support image. "
            "Leave empty if no image is uploaded or it is decorative."
        ),
    )

    # IT Protect
    protect_title = models.CharField(
        max_length=150,
        default="IT Protect",
        help_text="Heading for the second service card.",
    )
    protect_description = models.TextField(
        default=(
            "Discuss the protection of your practice computers "
            "and IT systems. Tell us what you currently have "
            "in place and any concerns, so we can explore "
            "your IT Protect requirements."
        ),
        help_text=(
            "Description of IT Protect. Replace this provisional "
            "introduction with the agreed offering. Only list "
            "protection features and coverage that are confirmed. "
            "Paragraph breaks are supported."
        ),
    )
    protect_image = models.ImageField(
        upload_to="it-support/",
        blank=True,
        help_text=(
            "Optional image for the IT Protect card. "
            "Use a landscape image suited to a 16:9 crop. "
            "Leave empty to show the card without an image."
        ),
    )
    protect_image_alt = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text=(
            "Describe the IT Protect image. "
            "Leave empty if no image is uploaded or it is decorative."
        ),
    )

    # Backup
    backup_title = models.CharField(
        max_length=150,
        default="Backup",
        help_text="Heading for the third service card.",
    )
    backup_description = models.TextField(
        default=(
            "Understand your practice's backup requirements "
            "and plan for situations where files or systems "
            "need to be restored. Talk to us about your "
            "existing arrangements, the information you "
            "depend on and your recovery priorities."
        ),
        help_text=(
            "Description of Backup. Confirm the available backup "
            "and recovery arrangements with Dmitry before listing "
            "specific features, retention periods or recovery times. "
            "Paragraph breaks are supported."
        ),
    )
    backup_image = models.ImageField(
        upload_to="it-support/",
        blank=True,
        help_text=(
            "Optional image for the Backup card. "
            "Use a landscape image suited to a 16:9 crop. "
            "Leave empty to show the card without an image."
        ),
    )
    backup_image_alt = models.CharField(
        max_length=255,
        blank=True,
        default="",
        help_text=(
            "Describe the Backup image. "
            "Leave empty if no image is uploaded or it is decorative."
        ),
    )

    # Shared card button
    card_link_text = models.CharField(
        max_length=100,
        default="Discuss your requirements",
        help_text=(
            "Link text shared by all three cards. "
            "Each link goes to the Contact page."
        ),
    )

    # Final call to action
    final_cta_eyebrow = models.CharField(
        max_length=100,
        default="Get in Touch",
        help_text="Small introductory label in the final dark panel.",
    )
    final_cta_title = models.CharField(
        max_length=255,
        default="Let's Discuss Your Practice IT",
        help_text="Main heading in the final call-to-action panel.",
    )
    final_cta_description = models.TextField(
        default=(
            "Whether you have a specific issue or are reviewing "
            "your support, protection and backup arrangements, "
            "tell us about your practice and what you need."
        ),
        help_text=(
            "Closing paragraph encouraging visitors to contact "
            "Dental Dynamix about their IT requirements."
        ),
    )
    final_cta_button_text = models.CharField(
        max_length=100,
        default="Get in Touch",
        help_text=(
            "Label for the final button. "
            "The button links to the Contact page."
        ),
    )

    # Admin details
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Automatically records when this page was last saved.",
    )

    class Meta:
        verbose_name = "IT Support Page"
        verbose_name_plural = "IT Support Page"

    def __str__(self):
        return "IT Support Page"

    def get_absolute_url(self):
        return reverse("it_support")

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)