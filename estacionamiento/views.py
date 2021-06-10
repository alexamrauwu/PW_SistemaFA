from .models import autos
from django.shortcuts import render

# Create your views here.
def index(request):
    #aqui = autos.objects.all()
    return render(request, 'vistas/login.html', {})

def mostrarAu(request):
    return render(request, 'vistas/autos.html', {})

#def mostrar(request):
 #   return render(request, 'vistas/login.html', {})

def re_autos(request):
    return render(request, 'vistas/re_autos.html', {})

def re_persona(request):
    return render(request, 'vistas/re_persona.html', {})


def registro(request):
    qs_autos = autos.objects.all()
    return render(request, 'vistas/registro.html', {'v_autos':qs_autos})

 