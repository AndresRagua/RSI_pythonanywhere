from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display=('nombre','conductor',)
    search_fields = ('nombre','conductor',)

@admin.register(Programacion)
class ProgramacionAdmin(admin.ModelAdmin):
    list_display=('nombre','fecha',)
    search_fields = ('nombre','fecha',)

@admin.register(Cania)
class CaniaAdmin(admin.ModelAdmin):
    list_display=('nombre',)
    search_fields = ('nombre',)

@admin.register(Contacto)
class ContactoAdmin(admin.ModelAdmin):
    list_display=('nombre','correo','numero')
    search_fields = ('nombre','correo')

@admin.register(Artista)
class ArtistaAdmin(admin.ModelAdmin):
    list_display=('nombre',)
    search_fields = ('nombre',)

@admin.register(Publicidad)
class PublicidadAdmin(admin.ModelAdmin):
    list_display=('nombre',)
    search_fields = ('nombre',)

@admin.register(UsuariosHilo)
class UsuariosHiloAdmin(admin.ModelAdmin):
    list_display=('nombre',)
    search_fields = ('nombre',)

#admin.site.register(Programa)
#admin.site.register(Contacto)