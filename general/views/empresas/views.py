from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from general.models import Empresa, Sucursal, Direccion, Cliente
from general.forms import EmpresaForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
import pandas as pd
import json
from django.db import connection


class EmpresaListView(LoginRequiredMixin, PermissionRequiredMixin ,  ListView):
    model = Empresa
    permission_required = 'general.view_empresa'
    permission_denied_message = 'No esta autorizado.'
    template_name='empresas/empresas.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'searchdata':
                data=[]
                for i in Empresa.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data, safe=False)

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Lista de Empresas'
        context['create_url']= reverse_lazy('general:EmpresaCreateViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['entity']= 'Empresas'
        return context

class EmpresaCreateView(LoginRequiredMixin, PermissionRequiredMixin ,CreateView):
    model=Empresa
    form_class= EmpresaForm
    template_name='empresas/create.html'
    permission_required = 'general.add_empresa'
    permission_denied_message = 'No esta autorizado.'
    success_url= reverse_lazy('general:EmpresaListViewpath')
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'add':
                form= EmpresaForm(request.POST)
                data= form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']= str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Creación de una Empresa'
        context['entity']= 'Empresas'
        context['list_url']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['action']='add'
        return context

class EmpresaUpdateView(LoginRequiredMixin, PermissionRequiredMixin ,UpdateView):
    model=Empresa
    form_class= EmpresaForm
    template_name='empresas/create.html'
    permission_required = 'general.change_empresa'
    permission_denied_message = 'No esta autorizado.'
    success_url= reverse_lazy('general:EmpresaListViewpath')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Edición de una Empresa'
        context['entity']= 'Empresas'
        context['list_url']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['action']='edit'
        return context

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'edit':
                form= self.get_form()
                data= form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']= str(e)
        return JsonResponse(data)

class EmpresaDetailView (DetailView):
    model = Empresa
    template_name = "empresas/detail.html"
     
    def get_context_data(self, **kwargs):
        context = super(EmpresaDetailView, self).get_context_data(**kwargs) 
        sucursales_s = Sucursal.objects.filter(id_empresa_id = self.object.id)
        clientes_s = Cliente.objects.filter(id_empresa_id = self.object.id)
        direciones_s = Direccion.objects.all()
        sucursales_values = Sucursal.objects.filter(id_empresa_id = self.object.id).values()

        print (sucursales_s)
        print (clientes_s)
        print (direciones_s)
        
        context['title']= 'Detalles de Empresa'
        context['entity']= 'Empresas'
        context['list_url']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['create_direcction']= reverse_lazy('general:DireccionesCreateViewpath')
        context['create_sucursals']= reverse_lazy('general:SucursalsCreateViewpath')
        context['create_cliente']= reverse_lazy('general:ClienteCreateViewpath')

        context['sucursales_s'] = sucursales_s
        context['direciones_s'] = direciones_s
        context['sucursales_values'] = sucursales_values
        context['clientes_s'] = clientes_s
        print (sucursales_values)

        return context


#Funcion para borrar logicamente

def borrar(request, id_empresa):
    try:
        if(request.method) == 'POST':
            data = request.POST
            val = data['active']
            if val == 'false':
                with connection.cursor() as cursor:
                    q = "UPDATE general_empresa SET empresa_activa = false WHERE id = " + str(id_empresa)
                    cursor.execute(q)
                return JsonResponse({"status" : "success", "code": "200"})
            else:
                with connection.cursor() as cursor:
                    q = "UPDATE general_empresa SET empresa_activa = true WHERE id = " + str(id_empresa)
                    cursor.execute(q)
                return JsonResponse({"status" : "success", "code": "200"})
    except Exception as e:
        data['error']= str(e)
        return JsonResponse(data)
