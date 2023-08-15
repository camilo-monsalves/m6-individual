from django.shortcuts import render

# modelos | importar modelo para desplegar en cliente.html
from .models import Cliente

# forms |
from .forms import ClienteForm


# Create your views here.

def landing(request):
    return render(request, 'OtroMundoApp/landing.html')

def cliente(request):
    contexto_cliente = {
        'clientes':Cliente.objects.all()
    }
    return render(request, 'OtroMundoApp/cliente.html', contexto_cliente)

def registro(request):
    if request.method == "POST":
        form_cliente = ClienteForm(request.POST)
        if form_cliente.is_valid():
            form_cliente.save()
    else:
        form_cliente = ClienteForm()
    return render(request=request, template_name='OtroMundoApp/registro.html', context={'form_cliente': form_cliente})
