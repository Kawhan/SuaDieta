from django.contrib import admin
from .models import Dieta

# Register your models here.
@admin.register(Dieta)
class DietaAdmin(admin.ModelAdmin):
    list_display = ['id', 'descricao', 'ingredientes', 'dieta_concluida']
    search_fields = ['id', 'descricao', 'ingredientes', 'dieta_concluida',]
    list_display_links = ['id', ]
    list_editable = ['dieta_concluida',]
    list_per_page = 20
    
    pass
    