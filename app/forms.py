from django import forms
from .models import Client, models
from django.contrib.auth.forms import UserCreationForm

class ConsultingForm(forms.Form):
    nomPatient = forms.CharField(max_length=100)
    poidPaient = forms.IntegerField()
    agePatient = forms.IntegerField()
    numeroWhatsApp = forms.CharField(max_length=20)
    desciptionProblem = forms.CharField(widget=forms.Textarea)

class VenteForm(forms.Form):
    nomClient = forms.CharField(label="Votre Nom", max_length=100, required=True)
    phoneClient = forms.CharField(label="Votre Numero", max_length=100, required=True)
    isLivrer = forms.BooleanField(label="Être Livrer", required=False)
    localisation = forms.CharField(label="Localisation", max_length=100, required=False)
    produit_id = forms.IntegerField(widget=forms.HiddenInput())
    quantite = forms.IntegerField(initial=1, widget=forms.HiddenInput())
    
    
# class ClientCreationForm(forms.Form):
#     firstname = forms.CharField()
#     lastname = forms.CharField()
#     numero = forms.CharField()
#     password = forms.CharField(widget=forms.PasswordInput)
#     confirm_password = forms.CharField(widget=forms.PasswordInput)

#     class Meta:
#         model = Client
#         fields = ['nom', 'prenom', 'telephone', 'password', 'confirm_password']

#     def clean(self):
#         cleaned_data = super().clean()
#         nom = cleaned_data.get("firstname")
#         telephone = cleaned_data.get("lastname")
#         numero = cleaned_data.get("numero")
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")

#         if password != confirm_password:
#             raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        
