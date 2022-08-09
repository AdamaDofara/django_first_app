from django.urls import path
from . import views
urlpatterns = [

    path('', views.liste_commande),
    path('ajout_commande', views.ajouter_commande, name="ajout_commande"),
    path('modification_commande/<str:pk>', views.modifier_commande, name="modifier_commande"),
    path('suppression_commande/<str:pk>', views.supprimer_commande, name="supprimer_commande")
]
