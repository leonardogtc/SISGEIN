from django.db import models


class Fornecedores(models.Model):
    nome_fantasia = models.CharField(
        max_length=150, verbose_name="Nome Fantasia")
    razao_social = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Razão Social")
    cnpj = models.CharField(max_length=14, unique=True, verbose_name="CNPJ")
    telefone = models.CharField(
        max_length=15, blank=True, null=True, verbose_name="Telefone de Contato")
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    site = models.URLField(blank=True, null=True, verbose_name="Site")

    def __str__(self):
        return self.nome_fantasia

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ['nome_fantasia']
