from django.test import TestCase
from django.urls import reverse
from .models import Categoria, Produto, Loja, Endereco, Cliente, Funcionario, Conta

# Create your tests here.

class TestarPaginasMain(TestCase):
    def test_pagina_inicial(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, 'Loja Virtual')

    def test_pagina_ajuda(self):
        response = self.client.get('/ajuda/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertContains(response, '<h2>Ajuda</h2>')

class TestarModelosMain(TestCase):
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
        self.endereco = Endereco.objects.create(
            logradouro='Rua A',
            numero='123',
            bairro='Centro',
            cidade='São Paulo',
            uf='SP',
            cep='01234567'
        )
        self.cliente = Cliente.objects.create(
            nome='João Silva',
            email='joao@example.com',
            telefone='11999999999',
            endereco=self.endereco
        )

    def test_categoria_str(self):
        self.assertEqual(str(self.categoria), 'Eletrônicos')

    def test_categoria_get_absolute_url(self):
        url = self.categoria.get_absolute_url()
        self.assertEqual(url, reverse('main:listar_produtos_por_categoria', args=[self.categoria.slug]))

    def test_produto_str(self):
        self.assertEqual(str(self.produto), 'Notebook')

    def test_produto_get_absolute_url(self):
        url = self.produto.get_absolute_url()
        self.assertEqual(url, reverse('main:detalhes_produto', args=[self.produto.id, self.produto.slug]))

    def test_endereco_str(self):
        expected = 'Rua A, 123 - São Paulo/SP'
        self.assertEqual(str(self.endereco), expected)

    def test_cliente_str(self):
        self.assertEqual(str(self.cliente), 'João Silva')

    def test_loja_str(self):
        loja = Loja.objects.create(
            nome='Loja Exemplo',
            endereco='Rua B, 456',
            cidade='Rio de Janeiro',
            uf='RJ',
            cep='20000000',
            email='loja@example.com'
        )
        self.assertEqual(str(loja), 'Loja Exemplo')

class TestarViewsMain(TestCase):
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

    def test_listar_produtos(self):
        response = self.client.get(reverse('main:listar_produtos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produto/listar.html')
        self.assertContains(response, 'Notebook')

    def test_listar_produtos_por_categoria(self):
        response = self.client.get(reverse('main:listar_produtos_por_categoria', args=[self.categoria.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produto/listar.html')
        self.assertContains(response, 'Notebook')

    def test_detalhes_produto(self):
        response = self.client.get(reverse('main:detalhes_produto', args=[self.produto.id, self.produto.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'produto/detalhes.html')
        self.assertContains(response, 'Notebook')

    def test_view_fale_conosco_get(self):
        response = self.client.get(reverse('fale_conosco'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'fale_conosco.html')

    def test_view_fale_conosco_post_valid(self):
        data = {
            'nome': 'Teste',
            'email': 'teste@example.com',
            'mensagem': 'Mensagem de teste'
        }
        response = self.client.post(reverse('fale_conosco'), data)
        self.assertEqual(response.status_code, 302)  # Redirect to success_url