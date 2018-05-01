from django.db import models


class Venda(models.Model):
    ENTRADA = 'EN'
    SAIDA = 'SA'
    TIPO_ENTRADA_CHOICES = (
        (ENTRADA, 'Entrada'),
        (SAIDA, 'Saída'),
    )

    data = models.DateField()
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    tipo_entrada = models.CharField(
        max_length=2,
        choices=TIPO_ENTRADA_CHOICES,
        default=ENTRADA,
    )

    def __str__(self):
        return str(self.data)
