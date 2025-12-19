from django.db import models
from django.urls import reverse


# Create your models here.

class Categoria(models.Model):
    nome = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=150, unique=True, db_index=True)
    data_criacao = models.DateTimeField(auto_now_add=True)  
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('nome',)
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'

    def __str__(self):
        return self.nome 
    
    def get_absolute_url(self):
        return reverse('main:listar_produtos_por_categoria', args=[self.slug])

# TAMANHOS = (
#     ('P', 'Pequeno'),
#     ('M', 'Médio'),
#     ('G', 'Grande'),
#     ('GG', 'Extra Grande'),
# )

class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', null=True, on_delete=models.CASCADE)
    nome = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=250, unique=True, db_index=True)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.PositiveIntegerField()
    disponivel = models.BooleanField(default=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_ultima_atualizacao = models.DateTimeField(auto_now=True)
    #tamanho = models.CharField(max_length=2, choices=TAMANHOS, default='M') 
    imagem = models.ImageField(upload_to='imagens-produtos', blank=True)

    class Meta:
        ordering = ('nome',)
        #index_together = (('id', 'slug'),) -> removido no Django 5.0, usar Index
        indexes = [
            models.Index(fields=['id', 'slug']),
        ]

    def __str__(self):
        return self.nome    
    
    def get_absolute_url(self):
        return reverse('main:detalhes_produto', args=[self.id, self.slug])

    # def save(self, *args, **kwargs):
    #     print('O método save foi chamado')
    #     print(f'Parâmetros: args={args}, kwargs={kwargs}')
    #     #executa o comportamento padrão de salvar
    #     super(Produto, self).save(*args, **kwargs)

    # def delete(self, *args, **kwargs):
    #     print('O método delete foi chamado')
    #     print(f'Parâmetros: args={args}, kwargs={kwargs}')
    #     #executa o comportamento padrão de deletar
    #     produto.delete()

class Loja(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=300)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)
    email = models.EmailField()
    produtos = models.ManyToManyField(Produto, blank=True)

    def __str__(self):
        return self.nome

class Endereco(models.Model):
    logradouro = models.CharField(max_length=200)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=100, blank=True)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    uf = models.CharField(max_length=2)
    cep = models.CharField(max_length=8)

    class Meta:
        indexes = [
            models.Index(fields=['cep'], name='idx_cep')
        ]
        indexes = [
            models.Index(fields=['cidade', 'uf'], name='idx_cidade_uf')
        ]

    def __str__(self):
        return f"{self.logradouro}, {self.numero} - {self.cidade}/{self.uf}"

class Cliente(models.Model):    
    nome = models.CharField(max_length=50)
    #endereco = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=50)
    cargo = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    telefone = models.CharField(max_length=15, blank=True)
    endereco = models.OneToOneField(Endereco, on_delete=models.CASCADE, primary_key=True)
    gerente = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nome

class Conta(models.Model):
    descricao = models.CharField(max_length=50)
    saldo = models.FloatField()
    superior = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"Conta de {self.cliente.nome} - Saldo: {self.saldo}"

class ItemMenu(models.Model):
    descricao = models.CharField(max_length=250)
    abreviatura = models.CharField(max_length=15)

    class Meta:
        abstract = True

