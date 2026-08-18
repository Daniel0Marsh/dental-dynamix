from django.db import models
from django_ckeditor_5.fields import CKEditor5Field


class OurSolutionsPage(models.Model):
    """
    Singleton model for the Our Solutions page content.
    """

    # =========================================================
    # Hero Section
    # =========================================================

    hero_image = models.ImageField(
        upload_to="solutions/",
        default="default/hero_image.webp",
        blank=True,
        help_text=(
            "Main hero image displayed at the top of the Our Solutions page."
        ),
    )

    hero_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Dental Dynamix providing complete dental technology, "
            "IT infrastructure, imaging and digital dentistry solutions"
        ),
        help_text=(
            "Alternative text for the hero image for SEO "
            "and accessibility."
        ),
    )

    hero_title = models.CharField(
        max_length=200,
        default="Complete Technology Solutions for Dental Practices",
        blank=True,
        help_text=(
            "Primary headline shown in the hero section."
        ),
    )

    hero_subtitle = models.CharField(
        max_length=300,
        default=(
            "From IT infrastructure and practice networks to digital imaging, "
            "CBCT, scanners, servers and specialist dental software, Dental "
            "Dynamix provides the technology, installation and support your "
            "practice needs."
        ),
        blank=True,
        help_text=(
            "Short supporting text displayed beneath the hero title."
        ),
    )


    # =========================================================
    # IT & Practice Infrastructure
    # =========================================================

    it_image = models.ImageField(
        upload_to="solutions/",
        default="default/our_it_image.webp",
        blank=True,
        help_text=(
            "Image representing Dental Dynamix IT infrastructure, "
            "networking, servers or technical services."
        ),
    )

    it_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Dental Dynamix providing IT infrastructure, computers, "
            "servers, networking and technical support for dental practices"
        ),
        help_text=(
            "Alternative text for the IT infrastructure image for SEO "
            "and accessibility."
        ),
    )

    it_title = models.CharField(
        max_length=200,
        default="IT & Practice Infrastructure",
        blank=True,
        help_text=(
            "Heading for the IT and infrastructure section."
        ),
    )

    it_text = CKEditor5Field(
        default=(
            "<p>Reliable dental technology starts with a reliable IT "
            "infrastructure. Dental Dynamix can provide everything from "
            "individual workstations and practice networks to servers, "
            "structured cabling and the infrastructure required to keep "
            "your practice connected.</p>"

            "<p>We can supply and configure PCs, servers, networking "
            "equipment, wireless networks and associated infrastructure, "
            "as well as installing and maintaining the systems that "
            "support your practice day to day.</p>"

            "<p>Whether you are opening a new practice, upgrading an "
            "existing site or need reliable ongoing IT support, we can "
            "provide a complete solution rather than leaving you to "
            "coordinate multiple suppliers.</p>"
        ),
        blank=True,
        help_text=(
            "Description of Dental Dynamix's IT infrastructure, "
            "networking and technical support services."
        ),
    )


    # =========================================================
    # Dental Imaging & Digital Dentistry
    # =========================================================

    imaging_image = models.ImageField(
        upload_to="solutions/",
        default="default/imaging_image.webp",
        blank=True,
        help_text=(
            "Image representing dental imaging, CBCT, X-ray, scanning "
            "or digital dentistry technology."
        ),
    )

    imaging_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Dental Dynamix supplying and supporting digital X-ray, "
            "CBCT, 2D and 3D dental imaging solutions"
        ),
        help_text=(
            "Alternative text for the dental imaging image for SEO "
            "and accessibility."
        ),
    )

    imaging_title = models.CharField(
        max_length=200,
        default="Dental Imaging & Digital Dentistry",
        blank=True,
        help_text=(
            "Heading for the dental imaging and digital dentistry section."
        ),
    )

    imaging_text = CKEditor5Field(
        default=(
            "<p>Dental Dynamix supplies and supports a wide range of "
            "digital dental imaging and digital dentistry technologies.</p>"

            "<p>From digital X-ray systems and 2D imaging through to "
            "CBCT and advanced 3D imaging solutions, we can help "
            "practices select, install and integrate the right equipment "
            "for their clinical requirements.</p>"

            "<p>We also support digital workflows including intraoral "
            "scanning and other connected technologies, helping practices "
            "make better use of their digital systems from image "
            "acquisition through to the software used to view, manage "
            "and work with the resulting information.</p>"
        ),
        blank=True,
        help_text=(
            "Description of Dental Dynamix's dental imaging and "
            "digital dentistry solutions."
        ),
    )


    # =========================================================
    # Equipment, Installation & Integration
    # =========================================================

    installation_image = models.ImageField(
        upload_to="solutions/",
        default="default/installation_image.webp",
        blank=True,
        help_text=(
            "Image representing equipment installation, dental equipment, "
            "integration or practice technology installation."
        ),
    )

    installation_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Dental Dynamix installing and integrating dental equipment, "
            "imaging systems, computers and practice technology"
        ),
        help_text=(
            "Alternative text for the equipment installation image "
            "for SEO and accessibility."
        ),
    )

    installation_title = models.CharField(
        max_length=200,
        default="Supply, Installation & Integration",
        blank=True,
        help_text=(
            "Heading for the equipment installation and integration section."
        ),
    )

    installation_text = CKEditor5Field(
        default=(
            "<p>Dental Dynamix does more than simply supply equipment. "
            "We can help manage the technology throughout the process, "
            "from selecting the right solution through to installation, "
            "configuration and ongoing support.</p>"

            "<p>This can include dental X-ray systems, CBCT equipment, "
            "intraoral scanners, computers, servers, networking "
            "infrastructure and the software required to connect "
            "everything together.</p>"

            "<p>Our understanding of both dental equipment and IT allows "
            "us to look at the practice as a complete technology "
            "environment rather than treating every system in isolation.</p>"

            "<p>For new practices, refurbishments and technology upgrades, "
            "we can help coordinate the technology required to create "
            "a reliable and integrated working environment.</p>"
        ),
        blank=True,
        help_text=(
            "Description of Dental Dynamix's equipment supply, "
            "installation and integration services."
        ),
    )


    # =========================================================
    # Software & Digital Workflows
    # =========================================================

    software_image = models.ImageField(
        upload_to="solutions/",
        default="default/software_image.webp",
        blank=True,
        help_text=(
            "Image representing dental software, digital workflows "
            "or connected practice technology."
        ),
    )

    software_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Dental Dynamix supporting dental software, imaging software "
            "and integrated digital workflows"
        ),
        help_text=(
            "Alternative text for the software image for SEO "
            "and accessibility."
        ),
    )

    software_title = models.CharField(
        max_length=200,
        default="Software & Digital Workflows",
        blank=True,
        help_text=(
            "Heading for the software and digital workflows section."
        ),
    )

    software_text = CKEditor5Field(
        default=(
            "<p>Modern dental practices rely on a wide range of software "
            "to manage patients, imaging, communication and clinical "
            "workflows. Dental Dynamix helps ensure the technology "
            "supporting these systems works together effectively.</p>"

            "<p>From imaging software and scanner workflows to practice "
            "systems and the computers and networks that support them, "
            "we can help with installation, configuration, connectivity "
            "and ongoing technical support.</p>"

            "<p>By understanding both the hardware and software within "
            "the practice, we can help identify problems and provide "
            "practical solutions without passing you between multiple "
            "suppliers.</p>"
        ),
        blank=True,
        help_text=(
            "Description of Dental Dynamix's software, integration "
            "and digital workflow support."
        ),
    )


    # =========================================================
    # Ongoing Support
    # =========================================================

    support_image = models.ImageField(
        upload_to="solutions/",
        default="default/support_image.webp",
        blank=True,
        help_text=(
            "Image representing ongoing technical support, maintenance "
            "or customer service."
        ),
    )

    support_image_alt_text = models.CharField(
        max_length=255,
        default=(
            "Dental Dynamix providing ongoing IT, dental technology "
            "and technical support to dental practices"
        ),
        help_text=(
            "Alternative text for the ongoing support image for SEO "
            "and accessibility."
        ),
    )

    support_title = models.CharField(
        max_length=200,
        default="Ongoing Support You Can Rely On",
        blank=True,
        help_text=(
            "Heading for the ongoing support section."
        ),
    )

    support_text = CKEditor5Field(
        default=(
            "<p>Technology does not stop working once it has been "
            "installed. Dental Dynamix provides ongoing technical "
            "support to help practices keep their systems running "
            "reliably.</p>"

            "<p>From everyday IT problems and network issues to "
            "troubleshooting imaging systems and supporting connected "
            "dental technology, our team can provide practical "
            "technical assistance when you need it.</p>"

            "<p>We aim to build long-term relationships with the "
            "practices we support, giving customers a trusted point "
            "of contact for their technology rather than relying on "
            "multiple disconnected suppliers.</p>"
        ),
        blank=True,
        help_text=(
            "Description of Dental Dynamix's ongoing technical "
            "support and maintenance services."
        ),
    )


    # =========================================================
    # Meta
    # =========================================================

    class Meta:
        verbose_name = "Our Solutions Page"
        verbose_name_plural = "Our Solutions Page"

    def __str__(self):
        return "Our Solutions Page"

    def save(self, *args, **kwargs):
        """
        Ensure only one Our Solutions page can exist.
        """
        if not self.pk and OurSolutionsPage.objects.exists():
            raise ValueError(
                "Only one Our Solutions Page can exist."
            )

        super().save(*args, **kwargs)