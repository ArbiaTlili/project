from django.urls import path
from . import views

urlpatterns = [
    path('agentsécurité',views.index, name="agentsécurité"),
    path('utilisateurs',views.utilisateurs, name="utilisateurs"),
    path('groupe',views.groupe, name="groupe"),
    path('droits',views.droits, name="droits"),
    path('privilège',views.privilège, name="privilège"),
    path('compte',views.compte, name="compte"),

    path('clientèle',views.index1, name="clientèle"),
    path('sousvoyage',views.sousvoyage, name="sousvoyage"),
    path('souscrédit',views.souscrédit, name="souscrédit"),
    path('compte1',views.compte1, name="compte1"),

    path('backoffice',views.index2, name="backoffice"),
    path('compagnies',views.compagnies, name="compagnies"),
    path('produit',views.produit, name="produit"),
    path('barémescrédit',views.barémescrédit, name="barémescrédit"),
    path('barémesvoyage',views.barémesvoyage, name="barémesvoyage"),
    path('décision',views.décision, name="décision"),
    path('compte2',views.compte2, name="compte2"),

    path('ajt_user/',views.ajt_user, name="ajt_user"),
]

