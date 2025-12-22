from django.shortcuts import get_object_or_404, render
from django.views.generic import FormView
from main import forms
from .models import Categoria, Produto
from carrinho.forms import FormAdicionarAoCarrinho

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
    
def listar_produtos(request, slug_categoria=None):
    categoria = None
    lista_categorias = Categoria.objects.all()
    lista_produtos = Produto.objects.filter(disponivel=True)
    if slug_categoria:
        categoria = get_object_or_404(Categoria, slug=slug_categoria)
        lista_produtos = Produto.objects.filter(categoria=categoria)
        
    contexto = {
        'categoria': categoria,
        'lista_categorias': lista_categorias,
        'lista_produtos': lista_produtos,
    }
    return render(request, 'produto/listar.html', contexto)

def detalhes_produto(request, id, slug_produto):
    produto = get_object_or_404(Produto, id=id, slug=slug_produto, disponivel=True)
    formulario_adicionar_ao_carrinho = FormAdicionarAoCarrinho()
    contexto = {'produto': produto, 'form_produto_carrinho': formulario_adicionar_ao_carrinho,}
    return render(request, 'produto/detalhes.html', contexto)