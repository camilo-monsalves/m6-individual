from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(help_text='Ingresa un email válido', required=True)

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']
        labels = {
            'first_name':'Nombre',
            'last_name':'Apellido',
            'username':'Nombre usuario',
            'email':'Correo electrónico',
            'password1':'Contraseña',
            'password2':'Repite la contraseña'
        }
    