from django.db import models

# Create your models here.
class Item(models.Model):
    preco = models.DecimalField(max_digits=8, decimal_places=2, blank=True)
    tamanho = models.CharField(max_length=50, blank=True)
    cor = models.CharField(max_length=50, blank=True)
    estoque = models.IntegerField(blank=True)
    descricao = models.TextField(blank=True)
    descricao_tecnica = models.TextField(blank=True)
    imagem = models.ImageField(upload_to='staticfiles/imagens/', blank=True)

    def __str__(self):
        return f"{self.descricao} - {self.cor} - {self.tamanho}"
