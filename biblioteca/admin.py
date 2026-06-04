from django.contrib import admin
from .models import Categoria, Autor, Editora, Livro, Emprestimo


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome', 'descricao')
    search_fields = ('nome',)


@admin.register(Autor)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')
    search_fields = ('nome',)


@admin.register(Editora)
class EditoraAdmin(admin.ModelAdmin):
    list_display = ('nome', 'site')
    search_fields = ('nome',)


@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    # exibiremos o título, a editora e a categoria na listagem principal
    list_display = ('titulo', 'editora', 'categoria',
                    'quantidade_disponivel', 'estado_conservacao')
    list_filter = ('categoria', 'editora', 'estado_conservacao')
    # Permite buscar pelo nome do autor também!
    search_fields = ('titulo', 'autores__nome')
    # filter_horizontal cria uma interface elegante para selecionar
    # múltiplos autores
    filter_horizontal = ('autores',)


@admin.register(Emprestimo)
class EmprestimoAdmin(admin.ModelAdmin):
    list_display = ('livro', 'aluno', 'funcionario', 'data_saida',
                    'data_devolucao_prevista', 'data_devolucao_real')
    list_filter = ('data_saida', 'data_devolucao_real')
    search_fields = ('aluno__nome', 'livro__titulo')
