from django.shortcuts import render

# Create your views here.

def index_page(request):
    print("test 1")
    return render(request, 'app/home.html')

def contact_page(request):
    print("contact")
    return render(request, 'app/contact.html')
def produits_page(request):
    print("produit")
    return render(request, 'app/produits.html')