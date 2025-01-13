from django import forms
from .models import Informa  # Import atualizado

class InformaForm(forms.ModelForm):  # Continua sendo o formulário
    class Meta:
        model = Informa
        fields = ['nome', 'email', 'whatsapp']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Digite seu nome'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Digite seu email'}),
            'whatsapp': forms.TextInput(attrs={'placeholder': 'Digite seu número do WhatsApp'}),
        }
