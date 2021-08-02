from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/index.html', context)

def utilisateurs(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/utilisateurs.html', context)

def groupe(request):
    return render(request, 'assurance/groupe.html')

def droits(request):
    return render(request, 'assurance/droits.html')

def privilège(request):
    return render(request, 'assurance/privilège.html')

def compte(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/compte.html', context)

def index1(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/index1.html', context)

def sousvoyage(request):
    return render(request, 'assurance/sousvoyage.html')

def souscrédit(request):
    return render(request, 'assurance/souscrédit.html') 

def compte1(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/compte1.html', context)       

def index2(request):
    context = {
        'welcome_text':"welcome index",
    }
    return render(request, 'assurance/index2.html',context)

def compagnies(request):
    context = {
        'welcome_text':"welcome c",
    }
    return render(request, 'assurance/compagnies.html', context)

def produit(request):
   
    return render(request, 'assurance/produit.html') 

def barémescrédit(request):
    return render(request, 'assurance/barémescrédit.html')  

def barémesvoyage(request):
    return render(request, 'assurance/barémesvoyage.html') 

def décision(request):
    return render(request, 'assurance/décision.html')
     
def compte2(request):
  
    return render(request, 'assurance/compte2.html')  

def ajt_user(request):
    context = {
        'welcome_text':"welcomecompte",
    }
    return render(request, 'assurance/utilisateurs.html', context)