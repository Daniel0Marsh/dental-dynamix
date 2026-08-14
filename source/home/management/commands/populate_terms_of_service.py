from django.core.management.base import BaseCommand
from home.models import TermsOfServicePage


class Command(BaseCommand):
    help = 'Populate Terms of Service page with sample content'

    def handle(self, *args, **options):
        content = """
        <h2>Effective Date: July 18, 2025</h2>
        <h2>Last Updated: July 18, 2025</h2>

        <p>Welcome to CodeBlock.io. By accessing or using our website, services, or development tools, you agree to these Terms of Service ("Terms"). Please read them carefully.</p>

        <h3>1. Acceptance of Terms</h3>
        <p>By using CodeBlock.io, you agree to comply with and be bound by these Terms and all applicable laws and regulations. If you do not agree with any part of the Terms, you may not use our services.</p>

        <h3>2. Use of Services</h3>
        <h4>a. Public Website Access</h4>
        <p>You are free to browse and explore the public portions of our site without creating an account. We do not collect personal data from visitors who simply access the site.</p>

        <h4>b. Developer Tools & Sandbox Access</h4>
        <p>To use certain features like:</p>
        <ul>
            <li>GitHub integration</li>
            <li>Online IDE or terminal access</li>
            <li>Project sandboxing</li>
            <li>Code collaboration tools</li>
        </ul>
        <p>you must authenticate via GitHub. By doing so, you grant us limited access to your public GitHub profile and repositories for the purpose of integrating with our platform. We do not access private repositories unless explicitly authorized.</p>

        <h3>3. Acceptable Use</h3>
        <p>You agree not to use our services to:</p>
        <ul>
            <li>Violate any applicable laws or regulations</li>
            <li>Infringe on intellectual property rights</li>
            <li>Transmit malicious code or malware</li>
            <li>Attempt to gain unauthorized access to our systems</li>
            <li>Interfere with the proper functioning of our services</li>
        </ul>

        <h3>4. Privacy and Data Protection</h3>
        <p>Your privacy is important to us. Please review our Privacy Policy, which also governs your use of our services and explains how we collect, use, and protect your information.</p>

        <h3>5. Intellectual Property</h3>
        <p>All content on CodeBlock.io, including but not limited to text, graphics, logos, and software, is the property of CodeBlock.io or its licensors and is protected by copyright and other intellectual property laws.</p>

        <h3>6. Limitation of Liability</h3>
        <p>CodeBlock.io shall not be liable for any indirect, incidental, special, consequential, or punitive damages, including without limitation, loss of profits, data, use, goodwill, or other intangible losses.</p>

        <h3>7. Changes to Terms</h3>
        <p>We reserve the right to modify these Terms at any time. We will notify users of any material changes by posting the new Terms on this page and updating the "Last Updated" date.</p>

        <h3>8. Contact Information</h3>
        <p>If you have any questions about these Terms of Service, please contact us at legal@codeblock.io.</p>
        """

        terms_of_service, created = TermsOfServicePage.objects.get_or_create(
            id=1,
            defaults={
                'content': content,
            }
        )

        if created:
            self.stdout.write(
                self.style.SUCCESS('Successfully created Terms of Service page with sample content')
            )
        else:
            terms_of_service.content = content
            terms_of_service.save()
            self.stdout.write(
                self.style.SUCCESS('Successfully updated Terms of Service page with sample content')
            ) 