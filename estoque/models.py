from django.db import models


class Fornecedor(models.Model):
    nome_fantasia = models.CharField(
        max_length=150, verbose_name="Nome Fantasia")
    razao_social = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="Razão Social")
    cnpj = models.CharField(max_length=14, unique=True, verbose_name="CNPJ")
    telefone = models.CharField(
        max_length=15, blank=True, null=True,
        verbose_name="Telefone de Contato"
    )
    email = models.EmailField(blank=True, null=True, verbose_name="E-mail")
    site = models.URLField(blank=True, null=True, verbose_name="Site")

    def __str__(self):
        return self.nome_fantasia

    class Meta:
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ['nome_fantasia']


class Produto(models.Model):
    UNIDADES_MEDIDA = (
        ('KG', 'Quilograma'),
        ('LT', 'Litro'),
        ('UN', 'Unidade'),
        ('CX', 'Caixa'),
    )

    nome = models.CharField(max_length=100, unique=True,
                            verbose_name="Nome do Produto")
    unidade_medida = models.CharField(
        max_length=2, choices=UNIDADES_MEDIDA,
        default='KG', verbose_name="Unidade de Medida")
    estoque_minimo = models.PositiveIntegerField(
        default=5, verbose_name="Estoque Mínimo (Alerta)")
    fornecedor_padrao = models.ForeignKey(
        Fornecedor, on_delete=models.SET_NULL, null=True, blank=True,
        related_name='produtos', verbose_name="Fornecedor Padrão")

    def __str__(self):
        return f"{self.nome} ({self.get_unidade_medida_display()})"

    # Propriedade inteligente para calcular o estoque total somando todos
    # os lotes
    @property
    def estoque_total(self):
        return sum(lote.quantidade_atual for lote in self.lotes.all())

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']


class Lote(models.Model):
    """
    Aqui reside a robustez do controle de perecíveis.
    Cada compra gera um lote com sua própria data de validade.
    """
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name="lotes",
        verbose_name="Produto"
    )
    identificador_lote = models.CharField(
        max_length=50,
        verbose_name="Número/Código do Lote"
    )
    quantidade_inicial = models.PositiveIntegerField(
        verbose_name="Quantidade Comprada"
    )
    quantidade_atual = models.PositiveIntegerField(
        verbose_name="Quantidade Atual em Estoque"
    )
    data_validade = models.DateField(
        verbose_name="Data de Validade"
    )
    data_entrada = models.DateField(
        auto_now_add=True, verbose_name="Data de Entrada"
    )

    def __str__(self):
        return f"Lote {self.identificador_lote} - {self.produto.nome} " \
            f"(Val: {self.data_validade})"

    class Meta:
        verbose_name = "Lote de Produto"
        verbose_name_plural = "Lotes de Produtos"
        ordering = ['data_validade']
