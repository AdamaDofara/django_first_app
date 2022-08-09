from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from commande.filtre import CommandeFiltre
from commande.form import CommandeForm
from commande.models import Commande

@login_required
def liste_commande(request):
    commandes = Commande.objects.all()
    myFiltre = CommandeFiltre(request.GET, queryset=commandes)
    commandes = myFiltre.qs
    context = {'commandes':commandes, 'myFiltre':myFiltre}
    return render(request, 'commande/liste_commande.html', context)

@login_required
def ajouter_commande(request):
    form = CommandeForm()
    if request.method == 'POST':
        form = CommandeForm(request.POST)
        if form.is_valid(): #est ce que les données du form sont valides
           form.save()
           return redirect('/')
    context ={'form':form}
    return render(request, 'commande/ajouter_commande.html', context)

@login_required
def modifier_commande(request, pk):
    commande = Commande.objects.get(id=pk)
    form = CommandeForm(instance=commande)

    if request.method == 'POST':
        form = CommandeForm(request.POST, instance=commande)
        if form.is_valid():
            # est ce que les données du form sont valides
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'commande/ajouter_commande.html', context)

@login_required
def supprimer_commande(request, pk):
    commande =  Commande.objects.get(id=pk)
    if request.method == 'POST':
        commande.delete()
        return redirect('/')
    context = {'item':commande}
    return render(request, 'commande/supprimer_commande.html', context)