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


class Turma(models.Model):
    # Usamos CharField para nomes como "6º Ano A" ou "Maternal II"
    nome = models.CharField(max_length=100, verbose_name='Nome da Turma')
    # PositiveIntegerField garante que o ano não seja negativo (ex: 2026)
    ano_letivo = models.PositiveIntegerField(verbose_name='Ano Letivo')

    def __str__(self):
        return f"{self.nome} ({self.ano_letivo})"

    class Meta:
        verbose_name = 'Turma'
        verbose_name_plural = 'Turmas'


class Aluno(models.Model):
    nome = models.CharField(max_length=100, verbose_name='Nome do Aluno')
    matricula = models.CharField(
        max_length=20, unique=True, verbose_name='Matrícula')
    data_nascimento = models.DateField(verbose_name='Data de Nascimento')
    email = models.EmailField(verbose_name='Email do Aluno')
    # Relacionamento Muitos-para-Muitos: Um aluno pode estar em mais de uma
    # turma, e uma turma obviamente tem muitos alunos.
    turmas = models.ManyToManyField(
        Turma, related_name='alunos', verbose_name='Turmas')

    def __str__(self):
        return f'{self.matricula} - {self.nome}'

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'
