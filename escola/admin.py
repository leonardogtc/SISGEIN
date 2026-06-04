from django.contrib import admin
from .models import Materia, Aluno, Turma


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')  # Colunas que aparecerão na listagem
    search_fields = ('nome',)  # Campo de busca


@admin.register(Turma)
class TurmaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'ano_letivo')  # Colunas que aparecerão na listagem
    search_fields = ('nome',)  # Campo de busca


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'matricula', 'data_nascimento',
                    'email')  # Colunas que aparecerão na listagem
    search_fields = ('nome', 'matricula')  # Campo de busca
    list_filter = ('data_nascimento',)  # Filtro lateral por data de nascimento
