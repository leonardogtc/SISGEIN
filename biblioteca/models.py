from django.db import models

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
