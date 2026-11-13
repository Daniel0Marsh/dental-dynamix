from .utils import build_meta


PAGE_DEFAULTS = {
    "/": (
        "Dental Imaging & Practice Technology | Dental Dynamix",
        "Explore dental imaging, equipment, software, IT support "
        "and servicing for dental practices from Dental Dynamix.",
    ),
    "/about/": (
        "About Dental Dynamix | Dental Technology",
        "Find out about Dental Dynamix and our work supporting "
        "dental practices with imaging, equipment and technology.",
    ),
    "/blog/": (
        "Dental Dynamix Blog | News & Insights",
        "Read the latest news, updates and insights on dental imaging, "
        "equipment, software and IT support from Dental Dynamix.",
    ),
    "/services/": (
        "Equipment Servicing & Repairs | Dental Dynamix",
        "Discuss dental equipment servicing, repairs, fault-finding "
        "and critical examination requirements with Dental Dynamix.",
    ),
    "/it-support/": (
        "Dental Practice IT Support | Dental Dynamix",
        "Discuss IT Support, IT Protect and Backup requirements "
        "for your dental practice with Dental Dynamix.",
    ),
    "/partners/": (
        "Dental Technology Partners | Dental Dynamix",
        "Explore our dental technology partners and their imaging "
        "equipment, software and practice solutions.",
    ),
    "/partners/products/": (
        "Dental Equipment & Software | Dental Dynamix",
        "Browse dental imaging equipment, X-ray systems, scanners "
        "and software from our technology partners.",
    ),
    "/contact/": (
        "Contact Dental Dynamix | Sales & Support",
        "Contact Dental Dynamix to discuss dental imaging, equipment, "
        "IT support and servicing requirements for your practice.",
    ),
    "/campaign/": (
        "Practice Technology Enquiries | Dental Dynamix",
        "Explore our current practice technology campaign and "
        "contact Dental Dynamix to register your interest.",
    ),
    "/remote-support/": (
        "Remote Support | Dental Dynamix",
        "Access the Dental Dynamix remote support page for "
        "assistance with your practice technology.",
    ),
    "/terms-and-conditions/": (
        "Terms and Conditions | Dental Dynamix",
        "View or download the Dental Dynamix Terms and Conditions.",
    ),
    "/privacy-policy/": (
        "Privacy Policy | Dental Dynamix",
        "View or download the Dental Dynamix Privacy Policy.",
    ),
    "/cookie-policy/": (
        "Cookie Policy | Dental Dynamix",
        "View or download the Dental Dynamix Cookie Policy.",
    ),
}


def seo_meta(request):
    title, description = PAGE_DEFAULTS.get(
        request.path,
        (
            "Dental Dynamix",
            "Dental imaging, equipment, software and practice technology.",
        ),
    )

    return {
        "meta": build_meta(request, title, description),
    }