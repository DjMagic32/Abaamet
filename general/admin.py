from django.contrib import admin
from .models import Sucursal, Cliente, Direccion, Empresa, Recepcion, Ingreso
# Register your models here.
admin.site.register(Sucursal),
admin.site.register(Cliente),
admin.site.register(Direccion),
admin.site.register(Empresa),
admin.site.register(Recepcion),
admin.site.register(Ingreso),

