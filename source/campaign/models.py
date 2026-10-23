
from django.db import models


class CampaignPage(models.Model):
    """
    Singleton content model for the campaign landing page.

    Controls campaign copy, homepage promotion copy, images,
    feature cards, registration guidance and CTA labels.
    The page layout remains defined in the templates.
    """

    # =========================================================
    # HERO SECTION
    # =========================================================

    hero_title = models.CharField(
        max_length=255,
        help_text="First line of the main hero heading.",
        default="Multiple locations.",
    )

    hero_title_highlight = models.CharField(
        max_length=255,
        help_text="Highlighted second line of the hero heading.",
        default="One connected practice.",
    )

    hero_subtitle = models.CharField(
        max_length=255,
        help_text="Supporting heading below the main hero title.",
        default="One imaging platform. Every patient. Every location.",
    )

    hero_description = models.TextField(
        help_text="Main introductory paragraph in the hero section.",
        default=(
            "Get an early look at DTX Studio Clinic powered by "
            "DTX Studio Go Sync. The intelligent imaging platform "
            "that connects 2D X-rays, CBCT scans, photos and treatment "
            "data across every location, giving your team access to "
            "the information they need to diagnose, plan and "
            "collaborate with confidence."
        ),
    )

    hero_highlight_text = models.CharField(
        max_length=100,
        help_text="Highlighted product name within the hero description.",
        default="DTX Studio Go Sync.",
    )

    hero_primary_button_text = models.CharField(
        max_length=100,
        help_text="Primary hero CTA label.",
        default="Register Your Interest",
    )

    hero_secondary_button_text = models.CharField(
        max_length=100,
        help_text="Secondary hero CTA label.",
        default="Discover Go Sync",
    )

    hero_eligibility_text = models.CharField(
        max_length=255,
        help_text="Short eligibility message below the hero buttons.",
        default=(
            "Early access opportunity for practices with 2–12 locations."
        ),
    )

    hero_image = models.ImageField(
        upload_to="campaigns/",
        help_text="Main campaign hero image.",
        default="default/campaign.webp",
    )

    hero_image_alt_text = models.CharField(
        max_length=255,
        help_text="Accessible description of the hero image.",
        default=(
            "Dental imaging technology for connected multi-location practices"
        ),
    )

    hero_support_title = models.CharField(
        max_length=255,
        help_text="Heading in the supporting message below the hero image.",
        default="Your practice, connected",
    )

    hero_support_description = models.TextField(
        help_text="Supporting message below the hero image.",
        default=(
            "Access patient imaging and treatment information "
            "across your practice locations."
        ),
    )

    # =========================================================
    # CAMPAIGN BENEFITS STRIP
    # =========================================================

    benefit_1_icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icons class for benefit 1, e.g. bi-cloud-check.",
        default="bi-cloud-check",
    )
    benefit_1_title = models.CharField(
        max_length=100,
        default="Connected Access",
    )
    benefit_1_description = models.CharField(
        max_length=255,
        default="Access imaging across locations",
    )

    benefit_2_icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icons class for benefit 2.",
        default="bi-diagram-3",
    )
    benefit_2_title = models.CharField(
        max_length=100,
        default="Connected Workflows",
    )
    benefit_2_description = models.CharField(
        max_length=255,
        default="Bring patient information together",
    )

    benefit_3_icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icons class for benefit 3.",
        default="bi-shield-check",
    )
    benefit_3_title = models.CharField(
        max_length=100,
        default="Secure Collaboration",
    )
    benefit_3_description = models.CharField(
        max_length=255,
        default="Support responsible information sharing",
    )

    benefit_4_icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icons class for benefit 4.",
        default="bi-people",
    )
    benefit_4_title = models.CharField(
        max_length=100,
        default="Multi-Site Practices",
    )
    benefit_4_description = models.CharField(
        max_length=255,
        default="Designed around connected teams",
    )

    # =========================================================
    # HOW IT WORKS SECTION
    # =========================================================

    how_it_works_eyebrow = models.CharField(
        max_length=255,
        default="One connected imaging platform",
    )

    how_it_works_title = models.CharField(
        max_length=255,
        help_text="Main heading for the how-it-works section.",
        default="The right patient information, wherever you work.",
    )

    how_it_works_description = models.TextField(
        help_text="Introductory paragraph for the how-it-works section.",
        default=(
            "Managing multiple practice locations shouldn't mean "
            "disconnected information. DTX Studio Go Sync is designed "
            "to help connect patient imaging and treatment information "
            "across your practice network."
        ),
    )
    how_it_works_image = models.ImageField(
        upload_to="campaigns/",
        help_text="Image for the how-it-works section.",
        default="default/campaign.webp",
    )

    how_it_works_image_alt_text = models.CharField(
        max_length=255,
        help_text="Accessible description for the how-it-works image.",
        default=(
            "Dental imaging technology supporting a connected "
            "multi-location practice"
        ),
    )

    how_it_works_button_text = models.CharField(
        max_length=100,
        help_text="CTA label for the how-it-works section.",
        default="Register Your Interest",    
    )

    # Feature 1
    feature_1_icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icons class for feature 1.",
        default="bi-images",
    )
    feature_1_title = models.CharField(
        max_length=255,
        default="Access connected imaging",
    )
    feature_1_description = models.TextField(
        default=(
            "Bring 2D X-rays, CBCT scans, clinical photographs and "
            "treatment information into a more connected multi-location workflow."
        ),
    )

    # Feature 2
    feature_2_icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icons class for feature 2.",
        default="bi-arrow-left-right",
    )
    feature_2_title = models.CharField(
        max_length=255,
        default="Reduce manual transfers",
    )
    feature_2_description = models.TextField(
        default=(
            "Help reduce the friction of disconnected workflows when "
            "teams need to work across different practice locations."
        ),
    )

    # Feature 3
    feature_3_icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icons class for feature 3.",
        default="bi-people",
    )
    feature_3_title = models.CharField(
        max_length=255,
        default="Support team collaboration",
    )
    feature_3_description = models.TextField(
        default=(
            "Help your teams access the information they need to "
            "coordinate care across your practice network."
        ),
    )

    # Feature 4
    feature_4_icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icons class for feature 4.",
        default="bi-grid-1x2",
    )
    feature_4_title = models.CharField(
        max_length=255,
        default="A workflow built around your practice",
    )
    feature_4_description = models.TextField(
        default=(
            "Explore how DTX Studio Go Sync could support the way "
            "your teams work across multiple locations."
        ),
    )

    # =========================================================
    # EARLY ACCESS REGISTRATION SECTION
    # =========================================================

    registration_eyebrow = models.CharField(
        max_length=255,
        default="Early Access Programme",
    )

    registration_title = models.CharField(
        max_length=255,
        default="Be among the first to experience it.",
    )

    registration_description = models.TextField(
        default=(
            "DTX Studio Go Sync is coming soon. We're inviting selected "
            "practices with 2–12 locations to register their interest."
        ),
    )

    registration_step_1_icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icons class for registration step 1.",
        default="bi-check-circle-fill",
    )

    registration_step_1_title = models.CharField(
        max_length=255,
        default="Tell us about your practice",
    )

    registration_step_1_description = models.TextField(
        default=(
            "Share a few details about your organisation and its locations."
        ),
    )

    registration_step_2_icon = models.CharField(
        max_length=100,
        help_text="Bootstrap Icons class for registration step 2.",
        default="bi-chat-dots",
    )

    registration_step_2_title = models.CharField(
        max_length=255,
        default="Speak with our team",
    )

    registration_step_2_description = models.TextField(
        default=(
            "We'll follow up to discuss your interest in the programme."
        ),
    )

    registration_partner_label = models.CharField(
        max_length=255,
        default="DEXIS Platinum Partner",
    )

    registration_partner_name = models.CharField(
        max_length=255,
        default="Dental Dynamix",
    )

    registration_form_title = models.CharField(
        max_length=255,
        default="Register your interest",
    )

    registration_form_description = models.TextField(
        default=(
            "Complete the form and our team will be in touch "
            "with further information."
        ),
    )

    # Registration form field labels
    form_first_name_label = models.CharField(
        max_length=100,
        default="First name *",
    )
    form_last_name_label = models.CharField(
        max_length=100,
        default="Last name *",
    )
    form_email_label = models.CharField(
        max_length=100,
        default="Work email address *",
    )
    form_phone_label = models.CharField(
        max_length=100,
        default="Telephone number",
    )
    form_practice_name_label = models.CharField(
        max_length=100,
        default="Practice or group name *",
    )
    form_locations_label = models.CharField(
        max_length=150,
        default="Number of practice locations *",
    )

    form_locations_placeholder = models.CharField(
        max_length=255,
        default="Enter number of locations",
    )

    form_locations_help_text = models.CharField(
        max_length=255,
        default=(
            "The early access programme is intended for practices "
            "with 2–12 locations."
        ),
    )

    form_submit_button_text = models.CharField(
        max_length=100,
        default="Submit Registration",
    )

    form_privacy_note = models.TextField(
        default=(
            "Your information will be used to respond to your "
            "early-access enquiry."
        ),
    )

    # =========================================================
    # HOMEPAGE: CURRENT PROMOTION
    # =========================================================

    current_promotion_eyebrow = models.CharField(
        max_length=255,
        help_text="Homepage label above the current-promotion heading.",
        default="Early Access Programme",
    )

    current_promotion_title = models.CharField(
        max_length=255,
        help_text="Homepage current-promotion section heading.",
        default="Connect Every Location with DTX Studio Go Sync",
    )

    current_promotion_description = models.TextField(
        help_text="Introductory paragraph above the homepage promotion card.",
        default=(
            "Discover how DTX Studio Go Sync can help multi-location "
            "dental practices connect patient imaging and treatment "
            "information across their practice network."
        ),
    )

    current_promotion_badge = models.CharField(
        max_length=100,
        default="Early Access",
    )

    current_promotion_card_eyebrow = models.CharField(
        max_length=255,
        default="For Multi-Location Practices",
    )

    current_promotion_card_title = models.CharField(
        max_length=255,
        default="One Imaging Platform. Every Location.",
    )

    current_promotion_card_description = models.TextField(
        default=(
            "Get an early look at DTX Studio Clinic powered by "
            "DTX Studio Go Sync. Register your interest to explore "
            "the programme for practices with 2–12 locations."
        ),
    )

    current_promotion_note = models.CharField(
        max_length=255,
        default="Register your interest in the early access programme.",
    )

    current_promotion_image = models.ImageField(
        upload_to="campaigns/promotions/",
        help_text="Optional dedicated image for the homepage promotion.",
        default="default/campaign.webp"
    )

    current_promotion_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "DTX Studio Go Sync connected dental imaging campaign"
        ),
    )

    # =========================================================
    # ADMIN / META
    # =========================================================

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Automatically updated when the campaign content changes.",
    )

    class Meta:
        verbose_name = "Campaign Page"
        verbose_name_plural = "Campaign Page"

    def __str__(self):
        return "Campaign Page"

    def save(self, *args, **kwargs):
        """Ensure that only one campaign page record exists."""
        self.pk = 1
        super().save(*args, **kwargs)
