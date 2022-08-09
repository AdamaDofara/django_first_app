from django.urls import path
from . import views
urlpatterns = [
    path('', views.getwebHookData, name="webhook"),
    path('/inscription', views.inscription, name="inscription"),
    path('/authentification', views.connexion, name="connexion"),
    path('/deconnexion', views.deconnexionUtilisateur, name='deconnexion')
    ]