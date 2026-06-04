from django.contrib import admin
from .models import GradeCurricular, Materia, Aluno, Turma


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')  # Colunas que aparecerão na listagem
    search_fields = ('nome',)  # Campo de busca


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_letivo')  # Colunas que aparecerão na listagem
    list_filter = ('ano_letivo',)  # Filtro lateral por ano letivo
    search_fields = ('nome',)  # Campo de busca


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'data_nascimento',
                    'email')  # Colunas que aparecerão na listagem
    search_fields = ('nome', 'matricula')  # Campo de busca
    # Interface de seleção horizontal para turmas
    # facilita a seleção de turmas em relacionamentos ManyToMany
    filter_horizontal = ('turmas',)


@admin.register(GradeCurricular)
class GradeCurricularAdmin(admin.ModelAdmin):
    # Colunas que aparecerão na listagem
    list_display = ('turma', 'materia', 'professor')
    list_filter = ('turma', 'materia',)  # Filtros lateral
