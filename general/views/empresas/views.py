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
        context['title']='Creacion de un Empresa'
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
        context['title']='Edicion de un Empresa'
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
        sucursales_s = Sucursal.objects.filter(id_empresa_id = self.object.id).values()
        clientes_s = Cliente.objects.filter(id_empresa_id = self.object.id).values()
        direciones_s = Direccion.objects.all().values()

        """ SE CREARON LOS DATAFRAMES CON LOS OBJETOS """
        direcciones_df = pd.DataFrame(direciones_s)
        sucursal_df = pd.DataFrame(sucursales_s)
        clientes_df = pd.DataFrame(clientes_s)
        print (clientes_df.get('sucursal_id_id'))

        if clientes_df.get('sucursal_id_id') is None:
            return clientes_df.get('sucursal_id_id')
        else:
            clientes_df['sucursal'] = clientes_df['sucursal_id_id']
            sucursal_df['sucursal'] = sucursal_df['id']
            direcciones_df['sucursal'] = direcciones_df['id']

            """ JOINT DE LAS 3 TABLAS """
            dataframe = clientes_df.set_index('sucursal').merge(sucursal_df.set_index('sucursal')).merge(direcciones_df.set_index('sucursal'))
            print (dataframe)
            """ PASAMOS EL DATAFRAME A JSON """
            json_df = dataframe.reset_index().to_json(orient ='records')
            data_json = []
            data_json = json.loads(json_df)
        
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
        context['action']='edit'
  
        """ CONTEXTO A JSON """
        #context['dataframe'] = dataframe.to_html()
        context['data_json'] = data_json
        #print (clientes.first().__dict__)

        return context
    
    