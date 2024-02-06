from django.db import models

# Create your models here.

# model de categories

class Categorie(models.Model):
        nomCategorie = models.CharField(max_length=255, unique=True)
        def __str__(self) -> str:
                return self.nomCategorie

# model de produit

class Produit(models.Model):
    nomPorduit = models.CharField(max_length=255)
    prixProduit = models.DecimalField(max_digits=10, decimal_places=2)
    quantite = models.IntegerField()
    descirpion = models.TextField()
    Categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomPorduit
  
#model pour la livraison

class Livraison(models.Model):
    
    nomLivreure = models.CharField(max_length=100,)
    phoneLivreure = models.CharField(max_length=20)
    
# model pour ventes

class Vente(models.Model):
    nomClient = models.CharField(max_length=255,)
    phoneClient = models.CharField(max_length=20)
    Produit = models.ForeignKey('Produit', on_delete=models.DO_NOTHING)
    quantite = models.PositiveIntegerField()
    isLivrer = models.BooleanField(default=False)
    dateVente = models.DateTimeField()
    livraison_id = models.ForeignKey("livraison",on_delete=models.DO_NOTHING)
    
    def montant_total(self):
        return self.produit.prixProduit * self.quantite
    
#model conseil

class Conseil(models.Model):
    titreConseil = models.CharField(max_length=255)
    descriptionConseil = models.TextField()
    
#model Consultation

class Consultation(models.Model):
    nomPatient = models.CharField(max_length=255)
    agePatient = models.PositiveIntegerField()
    phonePatient = models.CharField(max_length=20)
    desciptionProblem = models.TextField()