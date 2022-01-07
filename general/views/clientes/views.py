from django.http.response import JsonResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.edit import DeleteView
from general.models import Cliente
from general.forms import ClienteForm
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.utils.decorators import method_decorator
from django.contrib.auth.mixins import LoginRequiredMixin


class ClienteListView(LoginRequiredMixin, ListView):
    permission_required= ('general.view_cliente','general.add_cliente')
    model = Cliente
    template_name='clientes/clientes.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'searchdata':
                data=[]
                for i in Cliente.objects.all():
                    print (i)
                    data.append(i.toJSON())
            elif action == 'add':
                cli = Cliente()
                cli.nombre_completo = request.POST['nombre_completo']
                cli.telefono = request.POST['telefono']
                cli.telefono_ad = request.POST['telefono_ad']
                cli.email = request.POST['email']
                cli.id_empresa = request.POST['id_empresa']
                cli.save()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error']=str(e)
        return JsonResponse(data, safe=False)

    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Lista de Clientes'
        context['create_url']= reverse_lazy('general:ClienteCreateViewpath')
        context['list_url']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_prod']= reverse_lazy('general:ProductoListViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['entity']= 'Clientes'
        context['form']= ClienteForm()
        return context


class ClienteCreateView(LoginRequiredMixin, CreateView):
    model=Cliente
    form_class= ClienteForm
    template_name='clientes/create.html'
    #permission_required = 'general.add_empresa'
    #permission_denied_message = 'No esta autorizado.'
    success_url= reverse_lazy('general:ClienteListViewpath')
    

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        data={}
        try:
            action= request.POST['action']
            if action == 'add':
                form= ClienteForm(request.POST)
                data= form.save()
            else:
                data['error']='No ha ingresado a ninguna opcion'
        except Exception as e:
            data['error']= str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Creación de un Cliente'
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

class ClienteUpdateView(LoginRequiredMixin, UpdateView):
    model=Cliente
    form_class= ClienteForm
    template_name='clientes/create.html'
    success_url= reverse_lazy('general:ClienteListViewpath')

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)
    
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['title']='Edición de un Cliente'
        context['entity']= 'Clientes'
        context['list_url_recep']= reverse_lazy('general:RecepcionListViewpath')
        context['list_url']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_prod']= reverse_lazy('general:ClienteListViewpath')
        context['list_url_serv']= reverse_lazy('general:ServicioListViewpath')
        context['list_url_emp']= reverse_lazy('general:EmpresaListViewpath')
        context['list_url_dir']= reverse_lazy('general:DireccionesListViewpath')
        context['list_url_ingre']= reverse_lazy('general:IngresoListViewpath')
        context['list_url_cli']= reverse_lazy('general:ClienteListViewpath')
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
