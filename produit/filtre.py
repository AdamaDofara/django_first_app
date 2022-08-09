import django_filters

from produit.models import Produit


class ProduitFIltre(django_filters.FilterSet):
    class Meta:
        model = Produit
        fields = {'nom', 'prix'}