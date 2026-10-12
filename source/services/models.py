from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class ServicePage(models.Model):
    """
    Singleton model for the Service page content.
    """

    # =========================================================
    # Hero Section
    # =========================================================

    hero_image = models.ImageField(
        upload_to="services/",
        default="default/hero_image.webp",
        blank=True,
        help_text=(
            "Main hero image displayed at the top of the Service page."
        ),
    )

    hero_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Dental X-Ray Servicing & Repair - Dental Dynamix provides dental practices with the technology, equipment, imaging solutions and technical support they need to work smarter and deliver exceptional patient care."
        ),
        help_text=(
            "Alternative text for the hero image for SEO "
            "and accessibility."
        ),
    )

    hero_title = models.CharField(
        max_length=200,
        default="Dental X-Ray Servicing & Repair",
        blank=True,
        help_text=(
            "Primary headline shown in the hero section."
        ),
    )

    hero_subtitle = models.CharField(
        max_length=300,
        default=(
            "Support for the imaging equipment your practice relies on."
        ),
        blank=True,
        help_text=(
            "Short supporting text displayed beneath the hero title."
        ),
    )




    # =========================================================
    # SERVICES SECTION
    # =========================================================

    services_eyebrow = models.CharField(
        max_length=255,
        help_text="Small label displayed above the services heading.",
        default="IMAGING EQUIPMENT SUPPORT",
    )

    services_title = models.CharField(
        max_length=255,
        help_text="Main heading for the services section.",
        default="Keep your imaging equipment working reliably",
    )

    services_description = models.TextField(
        help_text="Introductory text displayed beside the services heading.",
        default="Talk to our team about planned servicing, fault diagnosis, and repair of your dental imaging equipment.",
    )

    #========================================================
    service_card_1_title = models.CharField(
        max_length=255,
        help_text="Title for service card one.",
        default="Planned Servicing",
    )

    service_card_1_description = models.TextField(
        help_text="Description for service card one.",
        default="Keep your imaging equipment working reliably and reduce the risk of unexpected downtime.",
    )

    #========================================================

    service_card_2_title = models.CharField(
        max_length=255,
        help_text="Title for service card two.",
        default="Fault Diagnosis",
    )

    service_card_2_description = models.TextField(
        help_text="Description for service card two.",
        default="Accurate fault diagnosis to help identify the cause of issues with your equipment.",
    )

    #========================================================

    service_card_3_title = models.CharField(
        max_length=255,
        help_text="Title for service card three.",
        default="Repair support",
    )

    service_card_3_description = models.TextField(
        help_text="Description for service card three.",
        default="Support with repairs, including sourcing parts and getting your equipment back up and running.",
    )





    # =========================================================
    # EQUIPMENT SECTION
    # =========================================================

    equipment_eyebrow = models.CharField(
        max_length=255,
        help_text="Small label displayed above the equipment heading.",
        default="your EQUIPMENT, OUR SUPPORT",
    )

    equipment_title = models.CharField(
        max_length=255,
        help_text="Main heading for the equipment section.",
        default="Support for your imaging systems",
    )

    equipment_description = models.TextField(
        help_text="Introductory text displayed beside the equipment heading.",
        default="",
        blank=True,
    )

    #========================================================
    equipment_card_1_title = models.CharField(
        max_length=255,
        help_text="Title for equipment card one.",
        default="Intraoral X-Ray",
    )

    equipment_card_1_description = models.TextField(
        help_text="Description for equipment card one.",
        default="Support for your wall and mobile X-ray systems used in general practice.",
    )

    equipment_card_1_image = models.ImageField(
        upload_to="home/",
        help_text="Image displayed in equipment card one.",
        default="default/equipment_card_1_image.webp"
    )

    equipment_card_1_image_alt_text = models.CharField(
        max_length=255,
        help_text="Alternative text for equipment card one image.",
        default="Dental intraoral X-ray technology services, support and repair",
    )

    #========================================================

    equipment_card_2_title = models.CharField(
        max_length=255,
        help_text="Title for equipment card two.",
        default="OPG & Panaramic",
    )

    equipment_card_2_description = models.TextField(
        help_text="Description for equipment card two.",
        default="Serviceing and repair support for your OPG and panoramic imaging systems.",
    )

    equipment_card_2_image = models.ImageField(
        upload_to="home/",
        help_text="Image displayed in equipment card two.",
        default="default/equipment_card_2_image.webp"
    )

    equipment_card_2_image_alt_text = models.CharField(
        max_length=255,
        help_text="Alternative text for equipment card two image.",
        default="Dental OPG and panoramic imaging technology services, support and repair",
    )

    #========================================================

    equipment_card_3_title = models.CharField(
        max_length=255,
        help_text="Title for equipment card three.",
        default="CBCT & 3D Imaging",
    )

    equipment_card_3_description = models.TextField(
        help_text="Description for equipment card three.",
        default="Support for CBCT and 3D imaging systems used in dental practices.",
    )

    equipment_card_3_image = models.ImageField(
        upload_to="home/",
        help_text="Image displayed in equipment card three.",
        default="default/equipment_card_3_image.webp"
    )

    equipment_card_3_image_alt_text = models.CharField(
        max_length=255,
        help_text="Alternative text for equipment card three image.",
        default="Dental CBCT and 3D imaging technology services, support and repair",
    )


    # =========================================================
    # SERVICE ENQUIRY SECTION
    # =========================================================

    service_enquiry_eyebrow = models.CharField(
        max_length=255,
        help_text="Small label displayed above the equipment heading.",
        default="Tell us what needs attention",
    )

    service_enquiry_title = models.CharField(
        max_length=200,
        default="Tell us what needs attention",
    )

    service_enquiry_description = models.TextField(
        default=(
            "To help us understand how we can support you, please provide "
            "your equipment make, model and a brief description of the fault or issue you are experiencing."
        ),
    )

    service_enquiry_item_1 = models.CharField(
        max_length=200,
        default="Image quality concerns",
    )

    service_enquiry_item_2 = models.CharField(
        max_length=200,
        default="Intermittent faults",
    )

    service_enquiry_item_3 = models.CharField(
        max_length=200,
        default="Error messages",
    )

    service_enquiry_item_4 = models.CharField(
        max_length=200,
        default="Routine service enquiries",
    )

    service_enquiry_contact_eyebrow = models.CharField(
        max_length=255,
        help_text="Small label displayed above the equipment heading.",
        default="Speak to our team",
    )

    service_enquiry_contact_title = models.CharField(
        max_length=200,
        default="Need help with your X-ray equipment?",
    )

    service_enquiry_contact_description = models.TextField(
        default="Tell us the make, model and issues so we can advice on the next steps.",
    )