from django.shortcuts import render
from django.views.generic import FormView
from main import forms

# Create your views here.

class ViewFaleConosco(FormView):
    template_name = 'fale_conosco.html'
    form_class = forms.FormFaleConosco
    success_url = '/'

    def form_valid(self, form):
        # Aqui você pode processar os dados do formulário, como enviar um e-mail
        nome = form.cleaned_data['nome']
        email = form.cleaned_data['email']
        mensagem = form.cleaned_data['mensagem']
        # Lógica para enviar e-mail ou salvar a mensagem pode ser adicionada aqui
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
    