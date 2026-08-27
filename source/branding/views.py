from django.shortcuts import render

from home.models import HomePage


def remote_support(request):
    home_page = HomePage.objects.first()

    return render(
        request,
        "remote_support.html",
        {
            "home": home_page,
        },
    )