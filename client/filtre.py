import django_filters

from client.models import Client


class CLientFiltre(django_filters.FilterSet):
    class Meta:
        model = Client
        fields = {'nom', 'telephone'}