from django.http import HttpResponse
from django.templatetags.static import static


def llms_txt(request):
    content = """# Dental Dynamix

> Dental Dynamix provides dental imaging technology, digital dentistry solutions, equipment, technical support, and related services for dental practices in the United Kingdom.

## Main pages

- [Home](https://dentaldynamix.co.uk/)
- [About](https://dentaldynamix.co.uk/about/)
- [Partners and Products](https://dentaldynamix.co.uk/partners/)
- [Contact](https://dentaldynamix.co.uk/contact/)
- [Remote Support](https://dentaldynamix.co.uk/remote-support/)
"""

    return HttpResponse(content, content_type="text/plain; charset=utf-8")