import json
import requests
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.decorators.csrf import csrf_exempt

from compte.form import CompteForm


def inscription(request):
    form = CompteForm()
    if request.method == 'POST':
        form = CompteForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request, 'Compte créé avec succès pour '+user)
            return redirect('/compte/authentification')
    context = {
    'form':form
    }
    return render(request, 'compte/inscription.html', context)

@csrf_exempt
def connexion(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        webhook_url ='http://127.0.0.1:50/'
        if user is not None:
            data = {'nom':username, 'pass':password, 'status':'utilisater connecte'}
            #data = json.loads(data)
            r = requests.post(webhook_url, data=json.dumps(data), headers={'Content-Type': 'application/json'})
            login(request, user)
            return redirect('accueil')
        else:
            messages.info(request, 'Utilisateur ou Mot de passe non correct(s)')
    context = {

    }
    return render(request, 'compte/connexion.html', context)


def deconnexionUtilisateur(request):
    logout(request)
    return redirect('connexion')

def getwebHookData(request):
    if request.method == 'POST':
        print("Donnee recu du Webhook est: ", request.body)
        return HttpResponse("Webhook recu!")
