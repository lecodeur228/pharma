from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import ConsultingForm, VenteForm
from .models import Categorie, Client, Conseil, Produit, Vente,Consultation
from datetime import datetime
import random
import string

# Create your views here.

def index_page(request):
    print("test 1")
    categories = Categorie.objects.all()
    conseils = Conseil.objects.all()
    context = {'categories': categories, 'conseils':conseils}
    return render(request, 'app/home.html',context)

def contact_page(request):
    print("contact")
    return render(request, 'app/contact.html')

def produits_page(request):
    print("produit")
    produits = Produit.objects.filter(quantite__gt=2)
    print(produits.count());
    context = {'produits': produits}
    return render(request, 'app/produits.html',context=context)

def produict_categorie_page(request, categorie_id):
    produits = Produit.objects.filter(Categorie=categorie_id)
    if not produits:
        message = "Aucun produit disponible pour cette catégorie."
        context = {'message': message}
    else:
        context = {'produits': produits}
    return render(request, 'app/produits.html',context=context)
    
def search_produit(request):
     query = request.GET.get('search')
     produits = Produit.objects.filter(nomProduit=query) 
     if not produits:
        message = f"Le medicament {query} n'est pas disponible chez nous"
        context = {'message': message}
     else:
        #  produits = Produit.objects.all()
         context = {'produits': produits, 'query': query}
     
     return render(request, 'app/produits.html',context=context)
 
def consulting_page(request):
    
    return render(request, 'app/consulting.html')
 
def post_consulting(request):
    if request.method == 'POST':
        form = ConsultingForm(request.POST)
        if form.is_valid():
          nomPatient = form.cleaned_data['nomPatient']     
          poidPaient = form.cleaned_data['poidPaient']     
          agePatient = form.cleaned_data['agePatient']     
          phonePatient = form.cleaned_data['numeroWhatsApp']     
          desciptionProblem = form.cleaned_data['desciptionProblem']
          consult = Consultation(nomPatient=nomPatient,poidPaient=poidPaient,agePatient=agePatient,phonePatient=phonePatient,desciptionProblem=desciptionProblem)
          consult.save()
          return redirect("consulting_page")
    else:
        form = ConsultingForm() 
        
    return render(request, 'app/consulting.html', {'form': form})

def single_produit(request,produit_id):
    produits = Produit.objects.filter(id=produit_id) 
    print(produits.count())
    context = {'produits': produits}
    return render(request, 'app/single_produit.html',context=context)

def generate_code_vente(length=4):
    characters = string.ascii_letters + string.digits
    random_code = ''.join(random.choice(characters) for _ in range(length))
    return random_code

def make_selling(request):
    if request.method == 'POST':
        form = VenteForm(request.POST)
        if form.is_valid():
            nom_client = form.cleaned_data['nomClient']
            phone_client = form.cleaned_data['phoneClient']
            livrer = form.cleaned_data['isLivrer']
            date_actuelle = datetime.now().date()
            if livrer:
                localisation = form.cleaned_data['localisation']
                if not localisation:
                    form.add_error('localisation', 'Veuillez fournir une localisation')
                    return render(request, 'template_form.html', {'form': form})
            produit_id = form.cleaned_data['produit_id']
            quantite = form.cleaned_data['quantite'] 
            code_vente = generate_code_vente()
            vente = Vente(nomClient=nom_client, phoneClient=phone_client, produit_id=produit_id, quantite=quantite, isLivrer=livrer,dateVente=date_actuelle,codevente=code_vente)
            vente.save()
            messages.success(request, f'Achate fait avec succès voici le code de recuperation du produits {code_vente}')
            # Rediriger vers la page précédente
            return redirect(request.POST.get('next', f'singleproduit/{produit_id}'))
    else:
        form = VenteForm()
    return render(request, 'single_produit.html', {'form': form})

def register_page(request):
    
    return render(request, 'app/register.html')

def login_page(request):
    
    return render(request, 'app/login.html')

def creer_client(request):
    if request.method == 'POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            telephone = form.cleaned_data['numero']
            mot_de_passe = form.cleaned_data['password']
            client = Client.objects.create(
                nom=nom,
                prenom=prenom,
                telephone=telephone,
                mot_de_passe=mot_de_passe
            )
            return redirect('')
    else:
        form = ClientCreationForm()
    return render(request, 'app/register.html', {'form': form})



# def register_view(request):
#     if request.method == 'POST':
#         form = ClientRegistrationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')  # Rediriger vers la page d'accueil après l'inscription
#     else:
#         form = ClientRegistrationForm()
#     return render(request, 'register.html', {'form': form})