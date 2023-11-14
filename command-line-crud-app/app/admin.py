from django.contrib import admin
from .models import Anime
# Register your models here.

@admin.register(Anime)
class AnimeAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)
    search_fields = ('name',)