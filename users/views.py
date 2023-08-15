from django.shortcuts import render, redirect
#1) importar messages
from django.contrib import messages

from django.contrib.auth import get_user_model, login

from .forms import UserRegistrationForm

# importar AuthenticationForm
from django.contrib.auth.forms import AuthenticationForm

# importar logout, login, authenticate
from django.contrib.auth import logout, login, authenticate

# importar login required
from django.contrib.auth.decorators import login_required
# Create your views here.

def registro_user(request):
    if request.user.is_authenticated:
        return redirect('/')
    
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('inicio')
        else:
            for error in list(form.errors.values()):
                print(request, error)
    else:
        form = UserRegistrationForm()

    return render(
        request=request,
        template_name="registro-user.html",
        context={"form":form}
    )
@login_required
def logout_user(request):
    logout(request)
    messages.success(request, f'Sesión finalizada correctamente')
    return redirect('inicio')

def login_user(request):
    if request.user.is_authenticated:
        return redirect('inicio')

    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {user.username}')
                return redirect('inicio')
        else:
            for error in list(form.errors.values()):
                messages.error(request, error)
    
    form = AuthenticationForm()

    return render(
        request=request,
        template_name='login-user.html',
        context={'form':form}
    )

