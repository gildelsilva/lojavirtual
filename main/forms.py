from django import forms
from django.core.mail import send_mail
from django.conf import settings

class FormFaleConosco(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100, required=True, initial="Seu nome aqui")
    email = forms.EmailField(label='Entre com seu e-mail:', required=True, initial="Seu e-mail aqui")
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea, required=True, initial="Digite sua mensagem aqui")      
    
    def enviar_email(self):
        send_mail('Fale Conosco: Mensagem de recebida', 
                  self.data['mensagem'],
                  self.data['email'], [settings.EMAIL_FALE_CONOSCO], fail_silently=False)