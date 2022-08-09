from django.urls import path
from . import views
urlpatterns = [
    path('client/<str:pk>', views.infoClient, name='infoClient'),
    path('ajout_client', views.ajoutClient, name='ajoutClient'),
    path('client', views.listeClient, name='listeClient'),
    path('api/getData', views.getData),
    path('api/addData', views.addData),
    path('api/detailData/<str:pk>', views.detailData),
    path('api/updateData/<str:pk>', views.updateData),
    path('api/deleteData/<str:pk>', views.deleteData)
]   
