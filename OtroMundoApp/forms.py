from django import forms
from .models import Cliente

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout
from crispy_bootstrap5 import bootstrap5

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente
        fields = ['nombre', 'apellido', 'pais', 'edad', 'hobby']
        widgets = {
            'hobby': forms.Textarea(attrs={'cols':30, 'rows':5}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.include_media = False
        self.helper.layout = Layout(
            bootstrap5.FloatingField("nombre", autocomplete="nombre"),
            bootstrap5.FloatingField("apellido", autocomplete="apellido")

        )
    



