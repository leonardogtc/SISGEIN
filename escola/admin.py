from django.contrib import admin
from .models import Materia, Aluno


@admin.register(Materia)
class MateriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')  # Colunas que aparecerão na listagem
    search_fields = ('nome',)  # Campo de busca
