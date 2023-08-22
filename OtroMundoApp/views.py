from django.shortcuts import render, redirect, get_object_or_404

# modelos | importar modelo para desplegar en cliente.html
from .models import Cliente

# forms |
from .forms import ClienteForm

# vistas genéricas Django
from django.views.generic import UpdateView, DeleteView

from django.contrib.auth.mixins import LoginRequiredMixin

from django.urls  import reverse, reverse_lazy

# messages
from django.contrib import messages

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

# sólo usuarios que pertenezcan al grupo moderador pueden eliminar un cliente.
class DeleteClienteView(LoginRequiredMixin, DeleteView):
    model = Cliente
    context_object_name = 'cliente'
    success_url = reverse_lazy('cliente')
    template_name = 'OtroMundoApp/cliente_delete.html'

    def test_func(self):
        return self.request.user.groups.filter(name='usuario_moderador').exists()

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "Debes iniciar sesión para eliminar un cliente.")
            return redirect(reverse('login-usuario'))
        if not self.test_func():
            messages.warning(request, 'Sólo moderadores pueden utilizar esta función')
            return redirect(reverse('cliente'))
        return super().dispatch(request, *args, **kwargs)


    def form_valid(self, form):
        messages.success(self.request, 'Cliente eliminado con éxito !')
        return super(DeleteClienteView, self).form_valid(form)


# sólo usuarios que pertenezcan al grupo moderador pueden editar datos de clientes.
class UpdateClienteView(LoginRequiredMixin, UpdateView):
    model = Cliente
    template_name = 'OtroMundoApp/cliente_update.html'
    fields = ['pais', 'edad', 'hobby']

    def test_func(self):
        return self.request.user.groups.filter(name='usuario_moderador').exists()

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.warning(request, "Debes iniciar sesión para actualizar un cliente.")
            return redirect(reverse('login-usuario'))
        if not self.test_func():
            messages.warning(request, 'Sólo moderadores pueden utilizar esta función')
            return redirect(reverse('cliente'))
        return super().dispatch(request, *args, **kwargs)
    

    def form_valid(self,form):
        nombre=form.instance.nombre
        apellido=form.instance.apellido 
        response = super().form_valid(form)
        messages.success(self.request, f'Cliente {nombre} {apellido} actualizado exitosamente!')
        return response

