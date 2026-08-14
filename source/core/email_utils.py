"""
Email utility functions for handling multiple email configurations
"""
from django.core.mail import EmailMessage
from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend


def get_bitcoin_email_backend():
    """
    Get the Bitcoin email backend configuration
    """
    return EmailBackend(
        host=settings.BITCOIN_EMAIL_HOST,
        port=settings.BITCOIN_EMAIL_PORT,
        username=settings.BITCOIN_EMAIL_HOST_USER,
        password=settings.BITCOIN_EMAIL_HOST_PASSWORD,
        use_tls=settings.BITCOIN_EMAIL_USE_TLS,
        fail_silently=False,
    )


def send_bitcoin_email(subject, message, recipient_list, html_message=None):
    """
    Send email using Bitcoin email configuration
    """
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.BITCOIN_FROM_EMAIL,
        to=recipient_list,
        connection=get_bitcoin_email_backend()
    )
    
    if html_message:
        email.content_subtype = 'html'
        email.body = html_message
    
    return email.send()


def send_company_email(subject, message, recipient_list, html_message=None):
    """
    Send email using company email configuration (default)
    """
    email = EmailMessage(
        subject=subject,
        body=message,
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=recipient_list
    )
    
    if html_message:
        email.content_subtype = 'html'
        email.body = html_message
    
    return email.send()


def send_email_by_context(subject, message, recipient_list, context='company', html_message=None):
    """
    Send email based on context
    context: 'company' or 'bitcoin'
    """
    if context == 'bitcoin':
        return send_bitcoin_email(subject, message, recipient_list, html_message)
    else:
        return send_company_email(subject, message, recipient_list, html_message) 