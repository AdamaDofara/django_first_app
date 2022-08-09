from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.
from client.clientForm import FormulaireCLient
from client.filtre import CLientFiltre
from client.models import Client
from commande.filtre import CommandeFiltre, CommandeFiltreByStatusAndProduit
from .serializers import ClientSerializer
# fonction de manipulation des api
@api_view(['GET'])
def getData(request):
    clients = Client.objects.all()
    serializer_class = ClientSerializer(clients, many=True)
    # person = {'name':'Adama','surname':'SILUE'}
    return Response(serializer_class.data)
@api_view(['POST'])
def addData(request):
    serializer_class = ClientSerializer(data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
    return Response(serializer_class.data)
@api_view(['GET'])
def detailData(request, pk):
    clients = Client.objects.get(id=pk)
    serializer_class = ClientSerializer(clients, many=False)
    return Response(serializer_class.data)

#api de modification
@api_view(['POST'])
def updateData(request, pk):
    client = Client.objects.get(id=pk)
    serializer_class = ClientSerializer(instance=client, data=request.data)
    if serializer_class.is_valid():
        serializer_class.save()
    return Response(serializer_class.data)
#api de suppression
@api_view(['DELETE'])
def deleteData(request,pk):
    client = Client.objects.get(id=pk)
    client.delete()
    return Response(client.nom+" delete avec succès")

def infoClient(request, pk):
    client = Client.objects.get(id=pk)
    commande = client.commande_set.all()
    commande_total = commande.count()
    #K9tN9GSULivfCFa mot de passe esygn
    myFilter = CommandeFiltreByStatusAndProduit(request.GET, queryset=commande)
    commande = myFilter.qs

    context={'client':client, 'commande':commande, 'commande_total':commande_total, 'myFilter':myFilter}
    return render(request, 'client/liste_client.html', context)

def ajoutClient(request):
    form = FormulaireCLient()
    if request.method == 'POST':
        form = FormulaireCLient(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request,'client/ajouter_client.html', context)


def listeClient(request):
    clients = Client.objects.all()
    filtreClient = CLientFiltre(request.GET, queryset=clients)
    clients=filtreClient.qs
    context = {'filtre':filtreClient, 'clients':clients}
    return render(request, 'client/client.html', context)

