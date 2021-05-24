from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import Tbbeneficiarios

@admin.register(Tbbeneficiarios)
class TbbeneficiariosAdmin(admin.ModelAdmin):
    list_display = ('nome',)