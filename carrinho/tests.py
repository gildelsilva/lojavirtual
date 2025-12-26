from django.test import TestCase, RequestFactory, Client
from django.urls import reverse
from decimal import Decimal
from main.models import Produto, Categoria
from .carrinho import Carrinho
from .forms import FormAdicionarAoCarrinho

# Create your tests here.

class TestarCarrinho(TestCase):
    def setUp(self):
        self.client = Client()
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
        self.carrinho = Carrinho(self.client)

    def test_adicionar_produto(self):
        self.carrinho.adicionar(self.produto, quantidade=2)
        self.assertEqual(len(self.carrinho), 2)
        self.assertIn(str(self.produto.id), self.carrinho.carrinho)

    def test_remover_produto(self):
        self.carrinho.adicionar(self.produto)
        self.assertEqual(len(self.carrinho), 1)
        self.carrinho.remover(self.produto)
        self.assertEqual(len(self.carrinho), 0)

    def test_limpar_carrinho(self):
        self.carrinho.adicionar(self.produto)
        self.carrinho.limpar_carrinho()
        self.assertEqual(len(self.carrinho), 0)

    def test_get_total_preco(self):
        self.carrinho.adicionar(self.produto, quantidade=2)
        total = self.carrinho.get_total_preco()
        self.assertEqual(total, Decimal('5000.00'))

    def test_iter_carrinho(self):
        self.carrinho.adicionar(self.produto, quantidade=1)
        items = list(self.carrinho)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['produto'], self.produto)
        self.assertEqual(items[0]['quantidade'], 1)
        self.assertEqual(items[0]['preco'], Decimal('2500.00'))
        self.assertEqual(items[0]['total_preco'], Decimal('2500.00'))

    def test_adicionar_produto(self):
        self.carrinho.adicionar(self.produto, quantidade=2)
        self.assertEqual(len(self.carrinho), 2)
        self.assertIn(str(self.produto.id), self.carrinho.carrinho)

    def test_remover_produto(self):
        self.carrinho.adicionar(self.produto)
        self.assertEqual(len(self.carrinho), 1)
        self.carrinho.remover(self.produto)
        self.assertEqual(len(self.carrinho), 0)

    def test_limpar_carrinho(self):
        self.carrinho.adicionar(self.produto)
        self.carrinho.limpar_carrinho()
        self.assertEqual(len(self.carrinho), 0)

    def test_get_total_preco(self):
        self.carrinho.adicionar(self.produto, quantidade=2)
        total = self.carrinho.get_total_preco()
        self.assertEqual(total, Decimal('5000.00'))

    def test_iter_carrinho(self):
        self.carrinho.adicionar(self.produto, quantidade=1)
        items = list(self.carrinho)
        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]['produto'], self.produto)
        self.assertEqual(items[0]['quantidade'], 1)
        self.assertEqual(items[0]['preco'], Decimal('2500.00'))
        self.assertEqual(items[0]['total_preco'], Decimal('2500.00'))

class TestarViewsCarrinho(TestCase):
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

    def test_adicionar_ao_carrinho_post(self):
        data = {'quantidade': 1, 'atualizar': False}
        response = self.client.post(reverse('carrinho:adicionar_ao_carrinho', args=[self.produto.id]), data)
        self.assertEqual(response.status_code, 302)  # Redirect

    def test_remover_do_carrinho(self):
        # Primeiro adicionar
        self.client.post(reverse('carrinho:adicionar_ao_carrinho', args=[self.produto.id]), {'quantidade': 1, 'atualizar': False})
        response = self.client.post(reverse('carrinho:remover_do_carrinho', args=[self.produto.id]))
        self.assertEqual(response.status_code, 302)

    def test_detalhes_carrinho_get(self):
        response = self.client.get(reverse('carrinho:detalhes_carrinho'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'carrinho/detalhes.html')
