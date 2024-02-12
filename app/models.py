from django.db import models


# Create your models here.

# model de categories

class Categorie(models.Model):
        nomCategorie = models.CharField(max_length=255, unique=True)
        def __str__(self) -> str:
                return self.nomCategorie

# model de produit

class Produit(models.Model):
    nomProduit = models.CharField(max_length=255)
    prixProduit = models.DecimalField(max_digits=10, decimal_places=2)
    photoProduit = models.ImageField(upload_to='photosProduits/', null=True, blank=True)
    quantite = models.IntegerField()
    descirpion = models.TextField()
    Categorie = models.ForeignKey('Categorie', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.nomProduit
  
#model pour la livraison

class Livraison(models.Model):
    
    nomLivreure = models.CharField(max_length=100,)
    phoneLivreure = models.CharField(max_length=20)
    
# model pour ventes


class Vente(models.Model):
    nomClient = models.CharField(max_length=255,)
    phoneClient = models.CharField(max_length=20)
    produit = models.ForeignKey('Produit', on_delete=models.DO_NOTHING)
    quantite = models.PositiveIntegerField()
    isLivrer = models.BooleanField(default=False)
    dateVente = models.DateTimeField()
    codevente = models.CharField(null=True)
    livraison_id = models.ForeignKey("livraison",on_delete=models.DO_NOTHING,null=True, blank=True)
    
    def montant_total(self):
        return self.produit.prixProduit * self.quantite
    
#model conseil

class Conseil(models.Model):
    titreConseil = models.CharField(max_length=255)
    descriptionConseil = models.TextField()
    
#model Consultation

class Consultation(models.Model):
    nomPatient = models.CharField(max_length=255)
    poidPaient = models.PositiveIntegerField(default=0) 
    agePatient = models.PositiveIntegerField()
    phonePatient = models.CharField(max_length=20)
    desciptionProblem = models.TextField()
    
class Client(models.Model):
    nom = models.CharField(max_length=255)
    prenom = models.CharField(max_length=255)
    telephone = models.CharField(max_length=20)
    mot_de_passe = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.prenom} {self.nom}"
