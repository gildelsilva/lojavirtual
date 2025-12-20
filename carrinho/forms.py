from django import forms

OPCOES_QUANTIDADE = [(i, str(i)) for i in range(1, 21)]

class FormAdicionarAoCarrinho(forms.Form):
    quantidade = forms.TypedChoiceField(choices=OPCOES_QUANTIDADE, coerce=int)
    atualizar = forms.BooleanField(required=False, widget=forms.HiddenInput)

    