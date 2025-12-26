from django.db import models
from decimal import Decimal
from main.models import Produto


# Create your models here.
class Pedido(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField()
    logradouro = models.CharField(max_length=100)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True)
    bairro = models.CharField(max_length=50)
    cep = models.CharField(max_length=20)
    cidade = models.CharField(max_length=50)
    uf = models.CharField(max_length=2)
    data_criacao = models.DateTimeField(auto_now_add=True)
    pago = models.BooleanField(default=False)

    class Meta:
        ordering = ('-data_criacao',)
    
    def __str__(self):
        return f'Pedido {self.id} - {self.nome}'
    
    def get_total_pedido(self):
        total = sum(item.get_total_item() for item in self.itens.all())
        return total
    
class ItemPedido(models.Model):
    pedido = models.ForeignKey(Pedido, related_name='itens', on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, related_name='itens_pedido', on_delete=models.CASCADE)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    quantidade = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'Item {self.id} do Pedido {self.pedido.id}'
    
    def get_total_item(self):
        return self.preco * self.quantidade
    