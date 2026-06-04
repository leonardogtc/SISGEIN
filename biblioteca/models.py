from django.db import models

from escola.models import Aluno
from django.conf import settings

# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True,
                            verbose_name='Nome da Categoria')
    descricao = models.TextField(
        blank=True, null=True, verbose_name='Descrição da Categoria')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class Autor(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nome do Autor'
    )
    nacionalidade = models.CharField(
        max_length=100,
        blank=True,
        null=True,
        verbose_name='Nacionalidade do Autor'
    )
    biografia = models.TextField(
        blank=True, null=True,
        verbose_name='Pequeno Histórico/Biografia do Autor'
    )
    foto = models.ImageField(
        upload_to='autores/',
        blank=True, null=True,
        verbose_name='Foto do Autor'
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Autor'
        verbose_name_plural = 'Autores'


class Editora(models.Model):
    nome = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Nome da Editora'
    )
    site = models.URLField(
        blank=True, null=True,
        verbose_name='Site da Editora'
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'


class Livro(models.Model):
    ESTADOS_CONSERVACAO = (
        ('EXC', 'Excelente'),
        ('REG', 'Regular (Marcas de uso)'),
        ('DAN', 'Danificado/Rasurado'),
    )
    titulo = models.CharField(
        max_length=200,
        verbose_name='Título do Livro'
    )
    capa = models.ImageField(
        upload_to='capas_livros/',
        blank=True, null=True,
        verbose_name='Capa do Livro'
    )
    quantidade_disponivel = models.PositiveIntegerField(
        default=1,
        verbose_name='Quantidade Disponível'
    )
    estado_conservacao = models.CharField(
        max_length=3,
        choices=ESTADOS_CONSERVACAO,
        default='EXC',
        verbose_name='Estado de Conservação'
    )
    # RELACIONAMENTOS ROBUSTOS:
    # Muitos para Muitos (Vários autores por livro)
    autores = models.ManyToManyField(
        Autor,
        related_name='livros',
        verbose_name='Autores do Livro'
    )
    editora = models.ForeignKey(
        Editora,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='livros',
        verbose_name='Editora do Livro'
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='livros',
        verbose_name='Categoria do Livro'
    )

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = 'Livro'
        verbose_name_plural = 'Livros'


class Emprestimo(models.Model):
    livro = models.ForeignKey(
        Livro,
        on_delete=models.CASCADE,
        related_name='emprestimos',
        verbose_name='Livro'
    )
    aluno = models.ForeignKey(
        Aluno, on_delete=models.CASCADE,
        related_name='emprestimos', verbose_name='Aluno'
    )
    funcionario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='emprestimos',
        verbose_name='Funcionário Responsável'
    )

    data_saida = models.DateField(
        auto_now_add=True, verbose_name="Data de Saída")
    data_devolucao_prevista = models.DateField(
        verbose_name="Data de Devolução Prevista")
    data_devolucao_real = models.DateField(
        null=True, blank=True, verbose_name="Data da Devolução Real")
    observacoes_danos = models.TextField(
        blank=True, null=True, verbose_name="Registro de Danos na Devolução")

    def __str__(self):
        return f"{self.livro.titulo} emprestado para {self.aluno.nome} " \
            f"em {self.data_saida.strftime('%d/%m/%Y')}"

    class Meta:
        verbose_name = 'Empréstimo'
        verbose_name_plural = 'Empréstimos'
        ordering = ['-data_saida']
