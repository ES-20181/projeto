from django.db import models

class Venda(models.Model):
    data = models.DateField(auto_now=False, auto_now_add=False)
    descricao = models.CharField(max_length=150)
    valor = models.DecimalField(max_digits=5, decimal_places=2)
    # Enquanto não tem os formulário prontos
    tipo = models.CharField(max_length=15)

    def __str__(self):
        return str(self.data)
