from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from main.models import Produto
from .forms import FormAdicionarAoCarrinho
from .carrinho import Carrinho

# Create your views here.

@require_POST

def adicionar_ao_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    form = FormAdicionarAoCarrinho(request.POST)
    if form.is_valid():
        quantidade = form.cleaned_data['quantidade']
        atualizar = form.cleaned_data['atualizar']
        carrinho.adicionar(produto=produto, quantidade=quantidade, atualizar_quantidade=atualizar)
    return redirect('carrinho:detalhes_carrinho')

def remover_do_carrinho(request, id_produto):
    carrinho = Carrinho(request)
    produto = get_object_or_404(Produto, id=id_produto)
    carrinho.remover(produto)
    return redirect('carrinho:detalhes_carrinho')   

def detalhes_carrinho(request):
    carrinho = Carrinho(request)
    for item in carrinho:
        item['form_adicionar'] = FormAdicionarAoCarrinho(initial={'quantidade': item['quantidade'], 'atualizar': True})
    return render(request, 'carrinho/detalhes.html', {'carrinho': carrinho})

