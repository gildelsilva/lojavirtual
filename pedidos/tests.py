from django.test import TestCase
from django.urls import reverse
from decimal import Decimal
from main.models import Produto, Categoria
from carrinho.carrinho import Carrinho
from .models import Pedido, ItemPedido
from .forms import FormCriarPedido

# Create your tests here.

class TestarModelosPedidos(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Eletrônicos', slug='eletronicos')
        self.produto = Produto.objects.create(
            categoria=self.categoria,
            nome='Notebook',
            slug='notebook',
            descricao='Um notebook potente',
            preco=2500.00,
            estoque=10,
            disponivel=True
        )
        self.pedido = Pedido.objects.create(
            nome='João Silva',
            email='joao@example.com',
            logradouro='Rua A',
            numero='123',
            bairro='Centro',
            cep='01234567',
            cidade='São Paulo',
            uf='SP',
            pago=False
        )
        self.item_pedido = ItemPedido.objects.create(
            pedido=self.pedido,
            produto=self.produto,
            preco=2500.00,
            quantidade=2
        )

    def test_pedido_str(self):
        self.assertEqual(str(self.pedido), f'Pedido {self.pedido.id} - João Silva')

    def test_pedido_get_total_pedido(self):
        total = self.pedido.get_total_pedido()
        self.assertEqual(total, Decimal('5000.00'))

    def test_item_pedido_str(self):
        self.assertEqual(str(self.item_pedido), f'Item {self.item_pedido.id} do Pedido {self.pedido.id}')

    def test_item_pedido_get_total_item(self):
        total = self.item_pedido.get_total_item()
        self.assertEqual(total, Decimal('5000.00'))

class TestarViewsPedidos(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome='Eletrônicos', slug='eletronicos')
        self.produto = Produto.objects.create(
            categoria=self.categoria,
            nome='Notebook',
            slug='notebook',
            descricao='Um notebook potente',
            preco=2500.00,
            estoque=10,
            disponivel=True
        )

    def test_criar_pedido_get(self):
        response = self.client.get(reverse('pedidos:criar_pedido'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pedidos/pedido/criar.html')

    def test_criar_pedido_post_valid(self):
        # Adicionar produto ao carrinho primeiro
        self.client.post(reverse('carrinho:adicionar_ao_carrinho', args=[self.produto.id]), {'quantidade': 1, 'atualizar': False})
        data = {
            'nome': 'João Silva',
            'email': 'joao@example.com',
            'logradouro': 'Rua A',
            'numero': '123',
            'complemento': '',
            'bairro': 'Centro',
            'cep': '01234567',
            'cidade': 'São Paulo',
            'uf': 'SP'
        }
        response = self.client.post(reverse('pedidos:criar_pedido'), data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pedidos/concluir.html')
        # Verificar se pedido foi criado
        self.assertTrue(Pedido.objects.filter(email='joao@example.com').exists())
