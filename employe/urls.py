from django.urls import path
from . import views

urlpatterns = [
    path('', views.effet_splash, name='effet_splash'),
    path('employes/', views.list_employe, name='list_employe'),
    path('ajouter/', views.ajouter_employe, name='ajouter_employe'),
    path('modifier/<int:employe_id>/', views.modifier_employe, name='modifier_employe'),
    path('supprimer/<int:employe_id>/', views.supprimer_employe, name='supprimer_employe'),
]
