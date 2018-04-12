from django.db import models

class Venda(models.Model):
    data = models.DateField()
    descricao = models.CharField(max_lenght=150)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    # Enquanto não tem os formulário prontos
    tipo = models.CharField(max_lenght=15)

    # def __str__(self):
    #     return self.data
