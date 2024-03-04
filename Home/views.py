from django.shortcuts import render
from django.http import HttpResponse
from .models import Hermes,Zara,Chanel,Traditional,Western,Kurtis,Paulmi,Hoodie,Lehanga,Night,Shirts,Track


def home(request):
    return render(request,'home.html')

def profile(request):
    return render(request, 'profile.html')
def hermes(request):
    products = Hermes.objects.all()
    context = {
        'Hermes': products
    }
    return render(request,'hermes.html',context)

def zara(request):  
    products = Zara.objects.all()
    context = {
        'Zara': products
    }
    return render(request, 'zara.html', context)



def chanel(request): 
    products = Chanel.objects.all()
    context = {
        'Chanel': products
    }
    return render(request,'chanel.html',context)

def ww(request): #women western
    products = Western.objects.all()
    context = {
        'Western': products
    }   
    return render(request,'ww.html',context)

def wt(request): #women traditional
    products = Traditional.objects.all()
    context = {
        'Traditional': products
    }  
    return render(request,'wt.html',context)

def lehangas(request): 
    products = Lehanga.objects.all()
    context = {
        'Lehanga': products
    }
    return render(request,'lehangas.html',context)

def kurtis(request): 
      products = Kurtis.objects.all()
      context = {
        'Kurtis': products
    }
      return render(request,'kurtis.html',context)


def night(request): 
     products = Night.objects.all()
     context = {
        'Night': products
    }
     return render(request,'night.html',context)

def hoodie(request): 
     products = Hoodie.objects.all()
     context = {
        'Hoodie': products
    }
     return render(request,'hoodie.html',context)

def paulmi(request): 
     products = Paulmi.objects.all()
     context = {
        'Paulmi': products
    }
     return render(request,'paulmi.html',context)

def shirts(request): 
     products = Shirts.objects.all()
     context = {
        'Shirts': products
    }
     return render(request,'shirts.html',context)

def track(request):
     products = Track.objects.all()
     context = {
        'Track': products
    } 
     return render(request,'track.html',context)









"""

def index(request):
    #return HttpResponse("<h1> Hey there! You're conneced with the django server <h1>")

def welcome(request):
    #return HttpResponse("Welcome! How r u?")

def connect(request):
    return HttpResponse("Connecting....")

def disconnect(request):
    return HttpResponse("Bye! See you later")
"""