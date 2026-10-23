
from django.db import models


class ServicePage(models.Model):
    """
    Singleton model for the Services page.
    All page copy, image selections and image alt text are editable
    through the Django admin.
    """

    # =========================================================
    # HERO SECTION
    # =========================================================

    hero_image = models.ImageField(
        upload_to="services/",
        default="default/hero_image.webp",
        help_text="Hero background image.",
    )
    hero_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Professional equipment servicing, repairs and technical support"
        ),
    )
    hero_title = models.CharField(
        max_length=255,
        default="Reliable Servicing, Repairs & Equipment Support",
    )
    hero_subtitle = models.TextField(
        default=(
            "From routine maintenance and fault-finding to equipment "
            "repairs, inspections and critical examinations for X-ray "
            "equipment, we help you keep your equipment safe, reliable "
            "and ready for use."
        ),
    )
    hero_primary_button_text = models.CharField(
        max_length=100,
        default="Enquire About Our Services",
    )


    # =========================================================
    # Trust Strip
    # =========================================================

    # Trust Strip - Item 1
    trust_1_title = models.CharField(
        max_length=100,
        default="Equipment Servicing",
    )
    trust_1_description = models.CharField(
        max_length=255,
        default="Planned maintenance and equipment care",
    )
    trust_1_icon = models.CharField(
        max_length=100,
        default="bi bi-gear",
    )

    # Trust Strip - Item 2
    trust_2_title = models.CharField(
        max_length=100,
        default="Repairs & Fault-Finding",
    )
    trust_2_description = models.CharField(
        max_length=255,
        default="Investigating faults and equipment breakdowns",
    )
    trust_2_icon = models.CharField(
        max_length=100,
        default="bi bi-tools",
    )

    # Trust Strip - Item 3
    trust_3_title = models.CharField(
        max_length=100,
        default="Critical Examinations",
    )
    trust_3_description = models.CharField(
        max_length=255,
        default="Enquiries about examinations for X-ray equipment",
    )
    trust_3_icon = models.CharField(
        max_length=100,
        default="bi bi-clipboard2-check",
    )

    # Trust Strip - Item 4
    trust_4_title = models.CharField(
        max_length=100,
        default="Technical Support",
    )
    trust_4_description = models.CharField(
        max_length=255,
        default="Practical advice and service guidance",
    )
    trust_4_icon = models.CharField(
        max_length=100,
        default="bi bi-wrench-adjustable",
    )


    # =========================================================
    # Services Overview
    # =========================================================

    # Services Overview - Section Heading
    overview_eyebrow = models.CharField(
        max_length=100,
        default="How We Can Help",
    )
    overview_heading = models.CharField(
        max_length=200,
        default="Equipment services to keep you moving",
    )
    overview_description = models.TextField(
        default=(
            "Whether you need routine maintenance, help diagnosing "
            "a fault or technical assistance, we can discuss your "
            "equipment and the most appropriate next step."
        ),
    )

    # Service Card 1 - Equipment Servicing
    overview_1_title = models.CharField(
        max_length=150,
        default="Equipment Servicing",
    )
    overview_1_image = models.ImageField(
        upload_to="services/",
        default="default/hero_image.webp",
    )
    overview_1_image_alt = models.CharField(
        max_length=255,
        default="Equipment undergoing routine servicing",
    )
    overview_1_icon = models.CharField(
        max_length=100,
        default="bi bi-gear",
    )
    overview_1_description = models.TextField(
        default=(
            "Planned servicing and preventative maintenance to help "
            "maintain equipment condition, support reliable operation "
            "and identify developing issues."
        ),
    )
    overview_1_link_text = models.CharField(
        max_length=100,
        default="Discuss servicing",
    )

    # Service Card 2 - Repairs and Fault-Finding
    overview_2_title = models.CharField(
        max_length=150,
        default="Repairs & Fault-Finding",
    )
    overview_2_image = models.ImageField(
        upload_to="services/",
        default="default/hero_image.webp",
    )
    overview_2_image_alt = models.CharField(
        max_length=255,
        default="Technical equipment inspection and fault diagnosis",
    )
    overview_2_icon = models.CharField(
        max_length=100,
        default="bi bi-tools",
    )
    overview_2_description = models.TextField(
        default=(
            "Assistance with equipment breakdowns, unexpected faults "
            "and performance issues to help establish the cause "
            "and appropriate corrective work."
        ),
    )
    overview_2_link_text = models.CharField(
        max_length=100,
        default="Discuss a repair",
    )

    # Service Card 3 - Inspections and Technical Support
    overview_3_title = models.CharField(
        max_length=150,
        default="Inspections & Technical Support",
    )
    overview_3_image = models.ImageField(
        upload_to="services/",
        default="default/hero_image.webp",
    )
    overview_3_image_alt = models.CharField(
        max_length=255,
        default="Technical equipment inspection and assessment",
    )
    overview_3_icon = models.CharField(
        max_length=100,
        default="bi bi-clipboard2-check",
    )
    overview_3_description = models.TextField(
        default=(
            "Discuss equipment checks, applicable testing and "
            "technical concerns to understand the work required "
            "and determine the next steps."
        ),
    )
    overview_3_link_text = models.CharField(
        max_length=100,
        default="Discuss your requirements",
    )


    # =========================================================
    # CRITICAL EXAMINATIONS FEATURE
    # =========================================================

    critical_eyebrow = models.CharField(
        max_length=255,
        default="Specialist Service",
    )
    critical_title = models.CharField(
        max_length=255,
        default="Critical examinations for X-ray equipment",
    )
    critical_description = models.TextField(
        default=(
            "Where equipment requires a critical examination, it is "
            "important to understand what is required, which system "
            "is involved and what arrangements need to be made."
        ),
    )
    critical_secondary_description = models.TextField(
        default=(
            "We provide a point of contact for enquiries about critical "
            "examinations for X-ray equipment. Contact us with the "
            "equipment details and your requirements so we can discuss "
            "the appropriate examination, scope of work and arrangements."
        ),
    )

    critical_bullet_1 = models.CharField(
        max_length=255,
        default="Enquiries about critical examinations for X-ray equipment.",
    )
    critical_bullet_2 = models.CharField(
        max_length=255,
        default=(
            "Discussion of the equipment, examination requirements "
            "and relevant circumstances."
        ),
    )
    critical_bullet_3 = models.CharField(
        max_length=255,
        default=(
            "Clear communication about the proposed scope of work "
            "and next steps."
        ),
    )

    critical_card_icon = models.CharField(
        max_length=100,
        default="bi bi-clipboard2-pulse",
    )
    critical_card_title = models.CharField(
        max_length=255,
        default="Arrange an Examination Enquiry",
    )
    critical_card_description = models.TextField(
        default=(
            "Tell us about the X-ray system, its location and the "
            "examination or service you require. We can then discuss "
            "the appropriate next step."
        ),
    )
    critical_button_text = models.CharField(
        max_length=150,
        default="Enquire About Critical Examinations",
    )
    critical_card_note = models.TextField(
        default=(
            "The applicable examination requirements, scope and "
            "arrangements will be confirmed for the equipment concerned."
        ),
    )


    # =========================================================
    # OUR APPROACH / PROCESS
    # =========================================================

    approach_eyebrow = models.CharField(
        max_length=255,
        default="The Process",
    )
    approach_title = models.CharField(
        max_length=255,
        default="From enquiry to next steps",
    )
    approach_description = models.TextField(
        default=(
            "A straightforward process to help establish what your "
            "equipment needs and how best to proceed."
        ),
    )

    approach_step_1_number = models.CharField(
        max_length=10,
        default="01",
    )
    approach_step_1_title = models.CharField(
        max_length=255,
        default="Tell Us About Your Equipment",
    )
    approach_step_1_description = models.TextField(
        default=(
            "Describe the equipment, any problems you have encountered "
            "and the service you require."
        ),
    )

    approach_step_2_number = models.CharField(
        max_length=10,
        default="02",
    )
    approach_step_2_title = models.CharField(
        max_length=255,
        default="Discuss the Requirements",
    )
    approach_step_2_description = models.TextField(
        default=(
            "We can clarify the equipment details, the issue "
            "and the work or examination involved."
        ),
    )

    approach_step_3_number = models.CharField(
        max_length=10,
        default="03",
    )
    approach_step_3_title = models.CharField(
        max_length=255,
        default="Establish the Next Steps",
    )
    approach_step_3_description = models.TextField(
        default=(
            "Discuss the proposed scope of work and any practical "
            "arrangements before proceeding."
        ),
    )



    # =========================================================
    # Preparing Your Enquiry
    # =========================================================

    # Preparing Your Enquiry - Section Heading
    enquiry_eyebrow = models.CharField(
        max_length=100,
        default="Before You Contact Us",
    )
    enquiry_heading = models.CharField(
        max_length=200,
        default="A few details can make all the difference",
    )
    enquiry_description = models.TextField(
        default=(
            "Providing some background helps us understand your "
            "requirements. Share whatever information you have "
            "available — you do not need to know the exact "
            "technical solution."
        ),
    )

    # Enquiry Detail 1 - Equipment Information
    enquiry_1_title = models.CharField(
        max_length=150,
        default="Equipment information",
    )
    enquiry_1_icon = models.CharField(
        max_length=100,
        default="bi bi-cpu",
    )
    enquiry_1_description = models.TextField(
        default=(
            "Machine type, manufacturer, model and serial number, "
            "if available."
        ),
    )

    # Enquiry Detail 2 - Service Required
    enquiry_2_title = models.CharField(
        max_length=150,
        default="The issue or service required",
    )
    enquiry_2_icon = models.CharField(
        max_length=100,
        default="bi bi-clipboard2-pulse",
    )
    enquiry_2_description = models.TextField(
        default=(
            "Fault symptoms, service history, error messages or "
            "details of the examination needed."
        ),
    )

    # Enquiry Detail 3 - Location and Timing
    enquiry_3_title = models.CharField(
        max_length=150,
        default="Location and timing",
    )
    enquiry_3_icon = models.CharField(
        max_length=100,
        default="bi bi-geo-alt",
    )
    enquiry_3_description = models.TextField(
        default=(
            "Where the equipment is installed and any deadlines "
            "or scheduling requirements."
        ),
    )

    # Enquiry Image
    enquiry_image = models.ImageField(
        upload_to="services/",
        default="default/hero_image.webp",
    )
    enquiry_image_alt = models.CharField(
        max_length=255,
        default="Technical specialist examining equipment",
    )


    # =========================================================
    # FINAL CALL TO ACTION
    # =========================================================

    final_cta_eyebrow = models.CharField(
        max_length=255,
        default="Get in Touch",
    )
    final_cta_title = models.CharField(
        max_length=255,
        default="Let's discuss your service requirements",
    )
    final_cta_description = models.TextField(
        default=(
            "From routine equipment servicing to repairs, technical "
            "support and critical examinations, contact us to discuss "
            "what you need."
        ),
    )
    final_cta_button_text = models.CharField(
        max_length=100,
        default="Get in Touch",
    )

    # =========================================================
    # ADMIN / META
    # =========================================================

    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="Automatically updated when the service page changes.",
    )

    class Meta:
        verbose_name = "Service Page"
        verbose_name_plural = "Service Page"

    def __str__(self):
        return "Service Page"

    def save(self, *args, **kwargs):
        """Ensure that only one ServicePage record exists."""
        self.pk = 1
        super().save(*args, **kwargs)
