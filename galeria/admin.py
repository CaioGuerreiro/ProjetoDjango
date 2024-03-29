from django.contrib import admin
from galeria.models import fotografia

# Register your models here.

class listandoFotografias(admin.ModelAdmin):
    list_display = ("id", "nome", "legenda", "publicada")
    list_display_links = ("id", "nome", "legenda")
    search_fields = ("nome",)
    list_filter = ("categoria","usuario",)
    list_editable = ("publicada",)
    list_per_page = 10

admin.site.register(fotografia, listandoFotografias)
