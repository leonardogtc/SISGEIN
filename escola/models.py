from django.db import models
from django.conf import settings


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


class GradeCurricular(models.Model):
    # Explicação: Cada entrada na grade curricular representa uma matéria que é
    # oferecida para uma turma específica. Assim, podemos ter "Matemática" na
    # "6º Ano A" e também na "7º Ano B", cada uma com sua própria entrada na
    # grade curricular.
    turma = models.ForeignKey(
        Turma,
        on_delete=models.CASCADE,
        related_name='grade_curricular',
        verbose_name='Turma'
    )
    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name='grade_curricular',
        verbose_name='Matéria'
    )

    # Buscamos o modelo de usuário configurado no settings (nosso CustomUser)
    """_summary_

    Returns:
        _type_: _description_

        Expliqueção: O campo "professor" é uma ForeignKey para o modelo de
        usuário, mas com um filtro específico para garantir que apenas
        usuários com o cargo de "PROF" (professor) possam ser selecionados.
        Isso é feito usando o argumento "limit_choices_to", que restringe as
        opções disponíveis no campo de seleção para apenas aqueles usuários
        que têm o cargo de professor. Dessa forma, garantimos que a grade
        curricular seja associada apenas a professores, evitando erros de
        associação com outros tipos de usuários, como diretores ou
        coordenadores.
    """
    professor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        # Filtro para listar apenas professores
        limit_choices_to={'cargo': 'PROF'},
        verbose_name="Professor"
    )

    def __str__(self):
        return f"{self.turma} - {self.materia.nome} ({self.professor.username})"

    class Meta:
        verbose_name = "Grade Curricular"
        verbose_name_plural = "Grades Curriculares"
        # Garante que não haverá a mesma matéria duplicada na mesma turma
        unique_together = ('turma', 'materia')
