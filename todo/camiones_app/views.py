from django.shortcuts import render
from .models import Balones
# Create your views here.
def listadobalones (request):
    losbalones=Balones.objects.all()
    return render(request,"gestionarcamiones.html",{"misbalones":losbalones})