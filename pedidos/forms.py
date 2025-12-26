
from .models import Pedido
from django import forms


class FormCriarPedido(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['nome', 'logradouro','numero', 'complemento', 'bairro', 'cidade', 'uf', 'cep', 'email']

