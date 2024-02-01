from django.shortcuts import render

# Create your views here.

def index_page(request):
    print("test 1")
    return render(request, 'app/home.html')