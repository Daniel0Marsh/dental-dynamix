from django.urls import path

from . import views


app_name = "partners"


urlpatterns = [
    path(
        "",
        views.partner_list,
        name="list",
    ),

    path(
        "products/",
        views.product_list,
        name="products",
    ),

    path(
        "<slug:slug>/",
        views.partner_detail,
        name="detail",
    ),
]