
from django.urls import path

from . import views

urlpatterns = [
    path("index", views.index_page, name="index"),
    path("contact", views.contact_page, name="contact_page"),
    path("produits", views.produits_page, name="produits_page"),
]