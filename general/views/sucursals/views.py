from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from general.models import Sucursal, Empresa
from general.forms import SucursalForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect,csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponseForbidden


class SucursalsListView(LoginRequiredMixin ,ListView):
    model = Sucursal
    template_name='sucursals/sucursals.html'
    #permission_required = 'general.view_direccion'
    #permission_denied_message = 'No esta autorizado.'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'searchdata':
                data=[]
                for i in Sucursal.objects.all():

                    print ('id', i.id_empresa.id)
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data, safe=False)

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Lista de Sucursales'
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['create_url']= reverse_lazy('general:SucursalsCreateViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['entity']= 'Sucursales'
        return context

class SucursalsCreateView(LoginRequiredMixin , CreateView):
    model=Sucursal
    form_class= SucursalForm
    template_name='sucursals/create.html'
    #permission_required = 'general.add_direccion'
    #permission_denied_message = 'No esta autorizado.'
    #success_url= reverse_lazy('general:DireccionesListViewpath')
    
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'add':
                form= SucursalForm(request.POST)
                data= form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']= str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Creacion de una Sucursal'
        context['entity']= 'Sucursales'
        context['list_url']= reverse_lazy('general:SucursalsListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['action']='add'
        return context

class SucursalsUpdateView(LoginRequiredMixin ,UpdateView):
    model= Sucursal
    form_class= SucursalForm
    template_name='sucursals/create.html'
    #permission_required = 'general.change_direccion'
    #permission_denied_message = 'No esta autorizado.'
    #success_url= reverse_lazy('general:DireccionesListViewpath')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Edicion de una Sucursal'
        context['entity']= 'Sucursales'
        context['list_url']= reverse_lazy('general:SucursalsListViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
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
    