from django.urls import path
from .views.forbidden.views import ForbiddenView
from .views.recepcion.views import RecepcionUpdateView
from .views.recepcion.views import RecepcionCreateView, RecepcionListView
from .views.empresas.views import *
from .views.direcciones.views import *
from .views.clientes.views import *
from .views.servicios.views import *
from .views.landing.views import *
from .views.productos.views import *
from .views.ingreso.views import *
from .views.sucursals.views import *

app_name='general'

urlpatterns = [
   path('principal/', LandingListView.as_view() , name='LandingPath'),
   path('principal/servicios', ServicioListView.as_view(), name='ServicioListViewpath'),
   path('principal/servicios/create/', ServicioCreateView.as_view(), name='ServicioCreateViewpath'),
   path('principal/servicios/edit/<int:pk>/', ServicioUpdateView.as_view(), name='ServicioUpdateViewpath'),
   
   path('principal/productos', ProductoListView.as_view(), name='ProductoListViewpath'),
   path('principal/productos/create/', ProductoCreateView.as_view(), name='ProductoCreateViewpath'),
   path('principal/productos/edit/<int:pk>/', ProductoUpdateView.as_view(), name='ProductoUpdateViewpath'),
   
   
   path('principal/clientes', ClienteListView.as_view(), name='ClienteListViewpath'),
   path('principal/clientes/create/', ClienteCreateView.as_view(), name='ClienteCreateViewpath'),
   path('principal/clientes/edit/<int:pk>/', ClienteUpdateView.as_view(), name='ClienteUpdateViewpath'),

   path('principal/direcciones', DireccionesListView.as_view(), name='DireccionesListViewpath'),
   path('principal/direcciones/create/', DireccionesCreateView.as_view(), name='DireccionesCreateViewpath'),
   path('principal/direcciones/edit/<int:pk>/', DireccionesUpdateView.as_view(), name='DireccionesUpdateViewpath'),

   path('principal/sucursals', SucursalsListView.as_view(), name='SucursalsListViewpath'),
   path('principal/sucursals/create/', SucursalsCreateView.as_view(), name='SucursalsCreateViewpath'),
   path('principal/sucursals/edit/<int:pk>/', SucursalsUpdateView.as_view(), name='SucursalsUpdateViewpath'),

   path('principal/empresas', EmpresaListView.as_view(), name='EmpresaListViewpath'),
   path('principal/empresas/create/', EmpresaCreateView.as_view(), name='EmpresaCreateViewpath'),
   path('principal/empresas/edit/<int:pk>/', EmpresaUpdateView.as_view(), name='EmpresaUpdateViewpath'),
   path('principal/empresas/detail/<int:pk>/', EmpresaDetailView.as_view(), name='EmpresaDetailViewpath'),
   path('principal/empresas/borrar/<int:id_empresa>/', borrar, name="EmpresaDeleteViewpath"),

   path('principal/recepcion', RecepcionListView.as_view(), name='RecepcionListViewpath'),
   path('principal/recepcion/create/', RecepcionCreateView.as_view(), name='RecepcionCreateViewpath'),
   path('principal/recepcion/edit/<int:pk>/', RecepcionUpdateView.as_view(), name='RecepcionUpdateViewpath'),

   path('principal/ingreso', IngresoListView.as_view(), name='IngresoListViewpath'),
]