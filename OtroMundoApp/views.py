from django.shortcuts import render

#importar modelo para desplegar en cliente.html
from .models import Cliente

# Create your views here.

def landing(request):
    return render(request, 'OtroMundoApp/landing.html')

def cliente(request):
    contexto_cliente = {
        'clientes':Cliente.objects.all()
    }
    return render(request, 'OtroMundoApp/cliente.html', contexto_cliente)