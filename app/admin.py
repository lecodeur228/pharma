from django import forms
from django.contrib import admin
from .models import Categorie, Produit, Vente,Conseil

# Register your models here.

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ("nomCategorie",)

class ProduitAdminForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Récupérer les catégories depuis la base de données
        categories = Categorie.objects.all()

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    form = ProduitAdminForm
    list_display =  ("nomProduit","photoProduit","prixProduit","quantite","descirpion","Categorie")
    
@admin.register(Vente)
class VenteAdmin(admin.ModelAdmin):
    list_display = ("nomClient","phoneClient","produit","quantite","isLivrer","dateVente","livraison_id")
    
@admin.register(Conseil)
class ConseilAdmin(admin.ModelAdmin):
    list_display = ("titreConseil","descriptionConseil")