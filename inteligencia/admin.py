from django.contrib import admin
from .models import PostGrad, NadaCosta, PlanoChamada
from django.utils.html import format_html

@admin.register(PostGrad)
class PostGradAdmin(admin.ModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    list_filter = ("title",)

@admin.register(NadaCosta)
class NadaCostaAdmin(admin.ModelAdmin):
    list_display = ("foto", "conduta", "post_grad", "re", "nome_guerra", "nome_completo", "opm", "subunidade", "situacao", "Consulta", "P2", "JD", "Observação", "updated_at")
    search_fields = ("re", "nome_guerra", "consulta", "p2", "jd")
    list_filter = ("conduta", "post_grad", "opm", "subunidade")
    list_display_links = ('re',)
    ordering = ('post_grad',)

    def foto(self, obj):
        if obj.imagem:
            return format_html(f'<a href="{obj.imagem.url} "><img src="{obj.imagem.url}" style="width:80px; height:107px" /></a>')
        return format_html('<img src="/media/placeholder.png" style="width:80px; height:107px" />')
    

@admin.register(PlanoChamada)
class PlanoChamadaAdmin(admin.ModelAdmin):
    list_display = ("foto", "post_grad", "re", "nome_guerra", "nome_completo", "subunidade", "logradouro", "numero", "complemento", "bairro", "municipio", "uf", "celulares", "telefone", "recado", "updated_at")
    search_fields = ("post_grad", "subunidade")
    list_display_links = ('re',)
    list_filter = ("subunidade",)

    def foto(self, obj):
        if obj.imagem:
            return format_html(f'<a href="{obj.imagem.url} "><img src="{obj.imagem.url}" style="width:80px; height:107px" /></a>')
        return format_html('<img src="/media/placeholder.png" style="width:80px; height:107px" />')