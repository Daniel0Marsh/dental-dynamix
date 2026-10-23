
import requests

from django.conf import settings
from django.contrib import messages
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.generic import TemplateView

from branding.models import Branding
from .models import CampaignPage


@method_decorator(never_cache, name="dispatch")
class CampaignPageView(TemplateView):
    """
    Display the campaign page and handle early-access registrations.
    """

    template_name = "campaign.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context.update({
            "branding": Branding.objects.first(),
            "campaign": CampaignPage.objects.first(),
            "CLOUDFLARE_TURNSTILE_SITE_KEY": (
                settings.CLOUDFLARE_TURNSTILE_SITE_KEY
            ),
        })

        return context

    def verify_turnstile(self, token, remote_ip=None):
        """
        Verify the Cloudflare Turnstile token server-side.
        """

        payload = {
            "secret": settings.CLOUDFLARE_TURNSTILE_SECRET_KEY,
            "response": token,
        }

        if remote_ip:
            payload["remoteip"] = remote_ip

        try:
            response = requests.post(
                "https://challenges.cloudflare.com/turnstile/v0/siteverify",
                data=payload,
                timeout=5,
            )
            response.raise_for_status()
            result = response.json()

            return result.get("success", False)

        except (requests.RequestException, ValueError):
            return False

    def post(self, request, *args, **kwargs):
        """
        Validate, verify and email an early-access registration.
        """

        # Only process the early-access form.
        if request.POST.get("form_type") != "early_access":
            messages.error(
                request,
                "Invalid form submission. Please try again.",
            )
            return redirect(f"{request.path}#early-access")

        # =========================================================
        # COLLECT FORM DATA
        # =========================================================

        form_data = {
            "first_name": request.POST.get("first_name", "").strip(),
            "last_name": request.POST.get("last_name", "").strip(),
            "email": request.POST.get("email", "").strip(),
            "phone": request.POST.get("phone", "").strip(),
            "practice_name": request.POST.get(
                "practice_name", ""
            ).strip(),
            "locations": request.POST.get("locations", "").strip(),
        }

        def invalid_form(message):
            messages.error(request, message)

            context = self.get_context_data()
            context["form_data"] = form_data

            return render(
                request,
                self.template_name,
                context,
                status=400,
            )

        # =========================================================
        # VALIDATE REQUIRED FIELDS
        # =========================================================

        required_fields = (
            "first_name",
            "last_name",
            "email",
            "practice_name",
            "locations",
        )

        if not all(form_data[field] for field in required_fields):
            return invalid_form(
                "Please complete all required fields."
            )

        # =========================================================
        # VALIDATE EMAIL
        # =========================================================

        from django.core.validators import validate_email
        from django.core.exceptions import ValidationError

        try:
            validate_email(form_data["email"])
        except ValidationError:
            return invalid_form(
                "Please enter a valid email address."
            )

        # =========================================================
        # VALIDATE NUMBER OF PRACTICE LOCATIONS
        # =========================================================

        try:
            locations = int(form_data["locations"])
        except (TypeError, ValueError):
            return invalid_form(
                "Please enter a valid number of practice locations."
            )

        if not 1 <= locations <= 100:
            return invalid_form(
                "The number of locations must be between 1 and 100."
            )

        # =========================================================
        # CLOUDFLARE TURNSTILE
        # =========================================================

        turnstile_token = request.POST.get(
            "cf-turnstile-response", ""
        ).strip()

        if not turnstile_token:
            return invalid_form(
                "Please complete the security verification."
            )

        if not self.verify_turnstile(
            turnstile_token,
            request.META.get("REMOTE_ADDR"),
        ):
            return invalid_form(
                "Security verification failed. Please try again."
            )

        # =========================================================
        # EMAIL NOTIFICATION
        # =========================================================

        subject = (
            "New Early Access Registration - "
            f"{form_data['practice_name']}"
        )

        message_content = (
            "A new early-access registration has been submitted.\n\n"
            f"First Name: {form_data['first_name']}\n"
            f"Last Name: {form_data['last_name']}\n"
            f"Email: {form_data['email']}\n"
            f"Phone: {form_data['phone'] or 'Not provided'}\n"
            f"Practice Name: {form_data['practice_name']}\n"
            f"Number of Locations: {locations}\n"
        )

        email_message = EmailMessage(
            subject=subject,
            body=message_content,
            from_email=settings.DEFAULT_FROM_EMAIL,
            to=[settings.SALES_EMAIL],
            reply_to=[form_data["email"]],
        )

        try:
            email_message.send(fail_silently=False)

        except Exception:
            # Log the exception server-side in production if needed.
            messages.error(
                request,
                "We couldn't submit your registration right now. "
                "Please try again later.",
            )

            context = self.get_context_data()
            context["form_data"] = form_data

            return render(
                request,
                self.template_name,
                context,
                status=500,
            )

        # =========================================================
        # SUCCESS
        # =========================================================

        messages.success(
            request,
            "Thank you! Your early-access registration has "
            "been submitted successfully.",
        )

        return redirect(f"{request.path}#early-access")
