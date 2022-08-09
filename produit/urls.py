from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='accueil'),
    path('produit', views.listeProduit, name='listeProduit')
]
