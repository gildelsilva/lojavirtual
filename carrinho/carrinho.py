from django.conf import settings
from decimal import Decimal
from main.models import Produto

class Carrinho:

    def __init__(self, request):
        self.request = request
        self.session = request.session
        carrinho = self.session.get(settings.ID_CARRINHO)
        if not carrinho:
            carrinho = self.session[settings.ID_CARRINHO] = {}
        self.carrinho = carrinho

    def adicionar(self, produto, quantidade=1, atualizar_quantidade=False):
        id_produto = str(produto.id)
        if id_produto not in self.carrinho:
            self.carrinho[id_produto] = {'quantidade': 0, 'preco': str(produto.preco)}
        if atualizar_quantidade:
            self.carrinho[id_produto]['quantidade'] = quantidade
        else:
            self.carrinho[id_produto]['quantidade'] += quantidade
        self.salvar()

    def salvar(self):
        self.session[settings.ID_CARRINHO] = self.carrinho
        self.session.modified = True
    
    def remover(self, produto):
        id_produto = str(produto.id)
        if id_produto in self.carrinho:
            del self.carrinho[id_produto]
            self.salvar()
    
    def limpar_carrinho(self):
        for key in self.session.keys():
                del self.session[key]
        self.session.modified = True

    def __iter__(self):
        id_produtos = self.carrinho.keys()
        produtos = Produto.objects.filter(id__in=id_produtos)
        carrinho = self.carrinho.copy()
        for produto in produtos:
            carrinho[str(produto.id)]['produto'] = produto
        for item in carrinho.values():
            item['preco'] = Decimal(item['preco'])
            item['total_preco'] = item['preco'] * Decimal(item['quantidade'])
            yield item
    
    def __len__(self):
        resultado = 0
        for item in self.carrinho.values():
            resultado += item['quantidade']
        return resultado
    
    def get_total_preco(self):
        resultado = Decimal(0.0)
        for item in self.carrinho.values():
            total_preco = Decimal(item['preco']) * Decimal(item['quantidade'])
            resultado += total_preco
        return resultado

