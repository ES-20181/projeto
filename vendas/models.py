from django.db import models

class Venda(models.Model):
    ENTRADA = 'EN'
    SAIDA = 'SA'
    MOVIMENTO_CAIXA_CHOICES = (
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saída'),
    )

    data = models.DateField()
    descricao = models.CharField()
    valor = models.DecimalField()
    tipo = models.CharField(
        max_length=2,
        choices=MOVIMENTO_CAIXA_CHOICES,
        default=ENTRADA,
    )

    def __str__(self):
        return self.data
