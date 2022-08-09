from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
# Create your views here.
from client.models import Client
from commande.models import Commande
from produit.filtre import ProduitFIltre
from produit.form import ProduitForm
from produit.models import Produit

@login_required
def home(request):
    commandes = Commande.objects.all()
    clients = Client.objects.all()
    context={'clients':clients,'commandes':commandes}
    return render(request, 'produit/accueil.html', context)
@login_required
def listeProduit(request):
    form = ProduitForm()
    if request.method == 'POST':
        form = ProduitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ProduitForm()
            messages.info(request, 'Produit ajouté avec succès')    
    produits = Produit.objects.all()
    myFiltre = ProduitFIltre(request.GET, queryset = produits)
    produits = myFiltre.qs
    context  = {
        'produits':produits,
        'filtre':myFiltre,
        'form':form
        }     
    return render(request, 'produit/produit.html', context)