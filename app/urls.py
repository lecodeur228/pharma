
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_page, name="index"),
    path("contact", views.contact_page, name="contact_page"),
    path("produits", views.produits_page, name="produits_page"),
    path("searchproduits", views.search_produit, name="search_produits_page"),
    path("singleproduit/<int:produit_id>/", views.single_produit, name="single_produit"),
    path("buyproduit", views.make_selling,name="buy_produit"),
    path("categories/<int:categorie_id>/", views.produict_categorie_page, name="categories"),
    path("consulting", views.consulting_page, name="consulting"),
    path("consultingpost", views.post_consulting, name="consultingpost"),
    path("register", views.register_page, name="register"),
    path("doregister", views.creer_client, name="do_register"),
    path("login", views.login_page, name="login"),
]