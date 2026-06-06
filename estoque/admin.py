from django.contrib import admin
from .models import Fornecedor, Produto, Lote
from django.utils.html import format_html
from datetime import date


@admin.register(Fornecedor)
class FornecedorAdmin(admin.ModelAdmin):
    list_display = ('nome_fantasia', 'cnpj', 'telefone', 'email')
    search_fields = ('nome_fantasia', 'cnpj')


@admin.register(Produto)
class PRodutoAdmin(admin.ModelAdmin):
    list_display = ('nome', 'unidade_medida',
                    'estoque_minimo', 'estoque_total')
    list_filter = ('unidade_medida',)
    search_fields = ('nome',)


@admin.register(Lote)
class LoteAdmin(admin.ModelAdmin):
    list_display = ('identificador_lote', 'produto',
                    'quantidade_atual', 'data_validade', 'status_validade')
    list_filter = ('data_validade', 'produto',)
    search_fields = ('identificador_lote', 'produto__nome')

    # Método customizado para gerar o alerta visual na tela
    def status_validade(self, obj):
        hoje = date.today()
        dias_para_vencer = (obj.data_validade - hoje).days
        if dias_para_vencer < 0:
            return format_html(
                '<span style="color: red; font-weight: bold;">Vencido</span>'
            )
        elif dias_para_vencer <= 15:
            return format_html(
                '<span style="color: orange; font-weight: bold;">Vence em {} '
                'dias</span>', dias_para_vencer
            )
        else:
            return format_html('<span style="color: green; font-weight: bold;">'
                               'Vence em {} dias</span>', dias_para_vencer)

    # Define o título da coluna no painel administrativo
    status_validade.short_description = "Status de Validade"
