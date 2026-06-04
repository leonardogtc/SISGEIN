from django.contrib import admin

from usuarios.models import Usuario

# Register your models here.


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    # Colunas que aparecerão na listagem
    list_display = ('username', 'cargo', 'cpf')
    search_fields = ('username', 'cpf')  # Campo de busca
    list_filter = ('cargo',)  # Filtro lateral por cargo
