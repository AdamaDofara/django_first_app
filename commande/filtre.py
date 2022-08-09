import django_filters

from commande.models import Commande


class CommandeFiltre(django_filters.FilterSet):
    class Meta:
        model = Commande
        fields = { 'status', 'produit', 'client'}

class CommandeFiltreByStatusAndProduit(django_filters.FilterSet):
    class Meta:
        model = Commande
        fields = ('produit', 'status')