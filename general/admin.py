from django.contrib import admin
from .models import Sucursal, Cliente, Direccion, Empresa, Recepcion, Ingreso
# Register your models here.

class EmpresaAdmin (admin.ModelAdmin):
    model =  Empresa
    list_display = ('id', 'nombre_empresa', 'nombre', 'numero_cliente', 'empresa_activa', 'rfc', 'num_client')

class SucursalAdmin (admin.ModelAdmin):
    model =  Sucursal
    list_display = ('id', 'nombre_sucursal', 'rfc', 'id_direccion', 'id_empresa', 'slug', 'contador_sucursales')

admin.site.register(Sucursal, SucursalAdmin),
admin.site.register(Cliente),
admin.site.register(Direccion),
admin.site.register(Empresa, EmpresaAdmin),
admin.site.register(Recepcion),
admin.site.register(Ingreso),
