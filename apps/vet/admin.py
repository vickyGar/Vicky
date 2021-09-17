from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

# -------------------------------------
class ResourceMascota(resources.ModelResource):
    class Meta:
        model = mascota

class AdminMascota(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ['pk_mascota', 'nombre', 'descripcion', 'raza', 'estado']
    resource_class = ResourceMascota

admin.site.register(mascota, AdminMascota)

# -------------------------------------
class ResourceCliente(resources.ModelResource):
    class Meta:
        model = cliente

class AdminCliente(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['telefono']
    list_display = ['pk_cliente', 'nombre_cliente', 'apellido_cliente', 'telefono', 'direccion']
    resource_class = ResourceCliente

admin.site.register(cliente, AdminCliente)

# -------------------------------------
class ResourceCita(resources.ModelResource):
    class Meta:
        model = Cita

class AdminCita(ImportExportModelAdmin, admin.ModelAdmin):
    search_fields = ['pk_cita']
    list_display = ['pk_cita', 'fk_cliente', 'fecha',  'fk_mascota']
    resource_class = ResourceCita

admin.site.register(Cita, AdminCita)