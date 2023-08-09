from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit
from crispy_bootstrap5.bootstrap5 import FloatingField
from django import forms
from .models import Cliente

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'pais', 'edad', 'hobby']
        widgets = {
            'hobby': forms.Textarea(attrs={'cols':30, 'rows':5}),
        }


    



