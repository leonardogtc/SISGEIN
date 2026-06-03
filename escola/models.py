from django.db import models


class Materia(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome da Matéria')
    descricao = models.TextField(
        blank=True, null=True, verbose_name='Ementa/Descrição')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Matéria'
        verbose_name_plural = 'Matérias'


class Aluno(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Aluno')
    matricula = models.CharField(
        max_length=20, unique=True, verbose_name='Matrícula')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    email = models.EmailField(verbose_name='Email do Aluno')

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
