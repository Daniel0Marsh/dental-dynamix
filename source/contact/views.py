import requests

from django.conf import settings
from django.contrib import messages
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.views.generic import TemplateView

from branding.models import Branding
from home.models import HomePage


class ContactPageView(TemplateView):
    """
    View for rendering and handling the contact page.
    """
    template_name = "contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            "branding": Branding.objects.first(),
            "home": HomePage.objects.first(),
            "CLOUDFLARE_TURNSTILE_SITE_KEY": (
                settings.CLOUDFLARE_TURNSTILE_SITE_KEY
            ),
        })

        return context

    def verify_turnstile(self, token, remote_ip=None):
        """
        Verify Cloudflare Turnstile token server-side.
        """
        payload = {
            "secret": settings.CLOUDFLARE_TURNSTILE_SECRET_KEY,
            "response": token,
        }

        if remote_ip:
            payload["remoteip"] = remote_ip

        response = requests.post(
            "https://challenges.cloudflare.com/turnstile/v0/siteverify",
            data=payload,
            timeout=5,
        )

        result = response.json()

        return result.get("success", False)

    def post(self, request):
        name = request.POST.get("name", "").strip()
        phone = request.POST.get("phone", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        enquiry_department = request.POST.get(
            "enquiry_department",
            ""
        ).strip()

        enquiry_type = request.POST.get(
            "enquiry_type",
            ""
        ).strip()

        # =========================================================
        # VALIDATE FORM
        # =========================================================

        if not all([
            name,
            phone,
            email,
            message,
            enquiry_department,
            enquiry_type,
        ]):
            messages.error(
                request,
                "Please fill in all the fields."
            )

            return render(
                request,
                self.template_name,
                self.get_context_data()
            )

        # =========================================================
        # VALIDATE ENQUIRY DEPARTMENT
        # =========================================================

        valid_departments = {
            "sales": "Sales",
            "support": "Support",
        }

        if enquiry_department not in valid_departments:
            messages.error(
                request,
                "Please select a valid enquiry type."
            )

            return render(
                request,
                self.template_name,
                self.get_context_data()
            )

        # =========================================================
        # VALIDATE ENQUIRY TYPE
        # =========================================================

        valid_enquiry_types = {
            "sales": {
                "imaging": "Dental Imaging & CBCT",
                "scanning": "Intraoral Scanning & Digital Dentistry",
                "equipment": "Equipment Supply & Installation",
                "software": "Software & Digital Workflows",
                "new_practice": "New Practice / Practice Refurbishment",
            },
            "support": {
                "it": "IT & Practice Infrastructure",
                "technical": "Technical Support",
                "software_support": "Software Support",
                "other": "Something Else",
            },
        }

        if enquiry_type not in valid_enquiry_types[enquiry_department]:
            messages.error(
                request,
                "Please select a valid enquiry option."
            )

            return render(
                request,
                self.template_name,
                self.get_context_data()
            )

        # =========================================================
        # DETERMINE RECIPIENT
        # =========================================================

        if enquiry_department == "sales":
            recipient_email = settings.SALES_EMAIL
        else:
            recipient_email = settings.SUPPORT_EMAIL

        # =========================================================
        # CLOUDflare TURNSTILE
        # =========================================================

        turnstile_token = request.POST.get(
            "cf-turnstile-response"
        )

        if not turnstile_token:
            messages.error(
                request,
                "Captcha verification failed. Please try again."
            )

            return render(
                request,
                self.template_name,
                self.get_context_data()
            )

        if not self.verify_turnstile(
            turnstile_token,
            request.META.get("REMOTE_ADDR"),
        ):
            messages.error(
                request,
                "Captcha verification failed. Please try again."
            )

            return render(
                request,
                self.template_name,
                self.get_context_data()
            )

        # =========================================================
        # HUMAN-READABLE VALUES
        # =========================================================

        department_display = valid_departments[
            enquiry_department
        ]

        enquiry_type_display = valid_enquiry_types[
            enquiry_department
        ][enquiry_type]

        # =========================================================
        # EMAIL
        # =========================================================

        subject = (
            f"{department_display} Enquiry - "
            f"{enquiry_type_display} - "
            f"{name}"
        )

        message_content = (
            f"New {department_display.lower()} enquiry\n"
            f"\n"
            f"Enquiry Type: {enquiry_type_display}\n"
            f"\n"
            f"Sender's Name: {name}\n"
            f"Sender's Phone: {phone}\n"
            f"Sender's Email: {email}\n"
            f"\n"
            f"Message:\n"
            f"{message}"
        )

        email_message = EmailMessage(
            subject=subject,
            body=message_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[recipient_email],
            reply_to=[email],
        )

        email_message.send(fail_silently=False)

        # =========================================================
        # SUCCESS
        # =========================================================

        messages.success(
            request,
            "Your message has been sent successfully!"
        )

        return render(
            request,
            self.template_name,
            self.get_context_data()
        )
    