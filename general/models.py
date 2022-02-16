from itertools import count
from pickle import FALSE
from re import T
from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.forms.models import model_to_dict
from django.utils import timezone
from django.contrib.auth.models import User
import collections
from datetime import date
from datetime import datetime


class EstadosMexico(models.TextChoices):

    aguascalientes ="Aguascalientes"
    baja_California ="Baja California"
    baja_California_Sur = "Baja California Sur"
    campeche = "Campeche"
    coahuila = "Coahuila"
    colima = "Colima"
    chiapas = "Chiapas"
    chihuahua = "Chihuahua"
    ciudad_de_Mexico = "Ciudad de Mexico"
    durango = "Durango"
    guanajuato = "Guanajuato"
    guerrero = "Guerrero"
    hidalgo = "Hidalgo"
    jalisco = "Jalisco"
    estado_de_Mexico = "Estado de Mexico"
    michoacan = "Michoacan"
    morelos = "Morelos"
    nayarit = "Nayarit"
    nuevo_Leon = "Nuevo Leon"
    oaxaca = "Oaxaca"
    puebla = "Puebla"
    queretaro = "Queretaro"
    quintana_Roo = "Quintana Roo"
    san_Luis_Potosi ="San Luis Potosi"
    sinaloa ="Sinaloa"
    sonora = "Sonora"
    tabasco = "Tabasco"
    tamaulipas = "Tamaulipas"
    tlaxcala = "Tlaxcala"
    veracruz = "Veracruz"
    yucatan = "Yucatan"
    zacatecas = "Zacatecas"

# Create your models here.
class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_empresa = models.CharField(max_length=150,verbose_name='Nombre de Empresa', null=True, blank=True)
    nombre = models.CharField(max_length=100, verbose_name='Nombre',  null=True, blank=True)
    numero_cliente = models.CharField(max_length=50, verbose_name='Numero de Cliente', editable = False)
    empresa_activa = models.BooleanField(default=True, null=True, verbose_name="activa") 
    rfc = models.CharField(null=True, max_length=30,verbose_name='RFC Empresa')
    num_client = models.CharField(null= True, blank=True, max_length=50, verbose_name='Numero de Cliente',)

    @property   
    def numero_cliente(self):
        check = str(self.nombre_empresa[0]).upper()
        empresa_filtro = list(Empresa.objects.filter(num_client__startswith = check).values_list('num_client', flat=True))

        if len(empresa_filtro) == 0:
            print ("no existe y es none")
            y = len(empresa_filtro) + 1
            y = str(y).zfill(3)
        else:
            print ("Se ejecuto el 'else'")
            x = empresa_filtro[-1]
            y = int(x[-1])
            y += 1
            y = str(y).zfill(3)

        return y

    @numero_cliente.setter
    def numero_cliente(self, value):
        self.numero_cliente = value


    def save(self, *args, **kwargs):
        if not self.id:
            self.num_client =  (str(self.nombre_empresa[0])).upper() + '-' + str(self.numero_cliente)
        return super(Empresa, self).save(*args, **kwargs)

    def __str__(self):
        return self.nombre_empresa
    def toJSON(self):
        item= model_to_dict(self)
        return item
    
    
class Direccion(models.Model):

    id = models.AutoField(primary_key=True)
    num_interior= models.CharField(max_length=80, verbose_name='Número Interior', blank=True , null= True )
    num_exterior= models.CharField(max_length=80, verbose_name='Número Exterior', blank=True , null= True )
    calle= models.CharField(max_length=50, verbose_name='Calle', blank=True , null= True )
    colonia= models.CharField(max_length=20, verbose_name='Colonia', blank=True , null= True )
    pais= models.CharField(max_length=15, verbose_name='Pais')
    referencia= models.CharField(max_length=254, verbose_name='Referencia', blank=True , null= True )
    localidad= models.CharField(max_length=30, verbose_name='Localidad', blank=True , null= True )
    estado= models.CharField(choices=EstadosMexico.choices , max_length=30, blank=True , null= True , verbose_name='Estado')
    municipio= models.CharField(max_length=20, verbose_name='Municipio', blank=True , null= True )
    codigo_postal= models.PositiveIntegerField(verbose_name='Código postal', blank=True , null= True )
    id_empresa = models.ForeignKey(Empresa, on_delete=DO_NOTHING, verbose_name='Empresa')
    def __str__(self):
        return self.localidad
    def toJSON(self):
        item= model_to_dict(self)
        return item

class Sucursal(models.Model):
    id= models.AutoField(primary_key=True)
    nombre_sucursal = models.CharField(null=True, max_length=50,verbose_name='Sucursal')
    rfc = models.CharField(null=True, max_length=30,verbose_name='RFC')
    id_direccion= models.ForeignKey(Direccion,null=True, blank=False, on_delete= DO_NOTHING,verbose_name='dirección')
    id_empresa = models.ForeignKey(Empresa, null=True, blank=False, on_delete=DO_NOTHING, verbose_name='Empresa')
    slug  = models.SlugField(blank=True, null=True, verbose_name='Numero de Cliente', editable=False)
    contador_sucursales = models.CharField(max_length=50, verbose_name='Numero de Cliente', editable=False)

    @property
    def contador_sucursales(self):
        exist_slug = Sucursal.objects.filter(id_empresa__id = self.id_empresa.id)

        return len(exist_slug)

    @contador_sucursales.setter
    def contador_sucursales(self, value):
        self.contador_sucursales = value

    def save(self, *args, **kwargs, ):
        if not self.id:
            sucursals_verify = Sucursal.objects.filter(id_empresa__id = self.id_empresa.id)
            var = int(self.contador_sucursales) + 1
            self.slug = (str(self.id_empresa.num_client)).upper() + '-' + str(var)

        return super(Sucursal, self).save(*args, **kwargs)


    def __str__(self):
        return self.nombre_sucursal
    def toJSON(self):
        item= model_to_dict(self)
        return item


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresa,null=True, blank=True, on_delete=DO_NOTHING,verbose_name='Empresa')
    nombre_completo = models.CharField(null=True,max_length=40,verbose_name='Nombre completo')
    telefono = models.CharField(max_length=12,verbose_name='Teléfono')
    telefono_ad = models.CharField(max_length=12,null=True,verbose_name='Teléfono Celular')
    email= models.EmailField(max_length=254,verbose_name='Email')
    sucursal_id = models.ForeignKey(Sucursal,null=True, blank=True, on_delete=DO_NOTHING,verbose_name='Sucursal')
    def __str__(self):
        return self.nombre_completo
    def toJSON(self):
        item= model_to_dict(self)
        return item
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    id_empresa = models.ForeignKey(Empresa,null=True, blank=True, on_delete=DO_NOTHING,verbose_name='empresa')
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    precio = models.PositiveIntegerField(verbose_name='Precio')
    marca = models.CharField(max_length=50,verbose_name='Marca')
    modelo = models.CharField(max_length=50,verbose_name='Modelo')
    detalle = models.TextField( verbose_name='Detalle')
    activo= models.BooleanField(verbose_name='Activo', default=True)
    def __str__(self):
        return self.nombre
    def toJSON(self):
        item= model_to_dict(self)
        return item
    class Meta:
        verbose_name='Producto'
        verbose_name_plural='Productos'
        db_table='g_producto'
        ordering= ['id']

class Servicio(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    precio = models.PositiveIntegerField(verbose_name='Precio')
    detalle = models.TextField( verbose_name='Detalle')
    activo= models.BooleanField(verbose_name='Activo', default=True)
    def __str__(self):
        return self.nombre
    def toJSON(self):
        item= model_to_dict(self)
        return item
    class Meta:
        verbose_name='Servicio'
        verbose_name_plural='Servicios'
        db_table='g_servicio'
        ordering= ['id']

class Cargo(models.Model):
    id=models.PositiveIntegerField(primary_key=True, verbose_name='id')
    nombre=models.CharField(max_length=100, verbose_name='Cargo')
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Cargo'
        verbose_name_plural='Cargos'
        db_table='g_cargo'
        ordering=['id']

""" ESTE MODELO NO SE ESTA UTILIZANDO, SE PUEDE REMOVER """
class Usuario(models.Model):
    id= models.PositiveIntegerField(primary_key=True, verbose_name='id')
    email= models.EmailField(verbose_name='Email')
    cargo= models.ForeignKey(Cargo,null=False, blank=False,on_delete=DO_NOTHING, verbose_name='Cargo')
    def __str__(self):
        return self.email
    class Meta:
        verbose_name='Usuario'
        verbose_name_plural='Usuarios'
        db_table='g_usuarios'
        ordering=['id']


class Cotizaciones(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    is_cliente = models.ForeignKey(Cliente,null=False,blank=False, on_delete=models.CASCADE)
    fecha_ini= models.DateField(null=False)
    fecha_fin= models.DateField(null=False)
    comentario = models.CharField(max_length=254)
    subtotal= models.FloatField(null=False)
    viaticos= models.FloatField(null=False)
    descuento = models.IntegerField(null=False)
    status= models.BooleanField(default=True)
    total_sin_iva= models.FloatField(null=False)

class Serv_Cot( models.Model):
    id_servicio= models.ForeignKey(Servicio,null=False, blank=False, on_delete=models.CASCADE)
    id_cotizacion= models.ForeignKey(Cotizaciones,null=False, blank=False, on_delete=models.CASCADE)



class Recepcion(models.Model):
    Paqueteria = 'Paqueteria'
    AbaaRecogio = 'Abaa Recogio'
    ClienteEntrego = 'Cliente Entrego'
    modoChoices = [
        (Paqueteria, 'Paqueteria'),
        (AbaaRecogio, 'AbaaRecogio'),
        (ClienteEntrego, 'ClienteEntrego'),
    ]
    Devuelto = 'Devuelto'
    Pendiente = 'Pendiente'
    Aprobado = 'Aprobado'
    estatusChoices = [
        (Devuelto, 'Devuelto'),
        (Pendiente, 'Pendiente'),
        (Aprobado, 'Aprobado'),
    ]
    

    n_entrada = models.CharField(max_length=50, verbose_name='Número de entrada', editable = False)
    nombre = models.CharField(max_length=50,verbose_name='Nombre')
    marca = models.CharField(max_length=50,verbose_name='Marca', blank=True , null= True)
    modelo = models.CharField(max_length=50,verbose_name='Modelo', blank=True , null= True)
    serie = models.CharField( verbose_name='Detalle',max_length=15, blank=True , null= True)
    identificacion= models.CharField(verbose_name='Identificación',max_length=10, blank=True , null= True)
    descripcion_particular = models.CharField(verbose_name='Descripción particular',max_length=25, blank=True , null= True)
    fecha_de_recepcion = models.DateTimeField(auto_now_add= True)
    modified = models.DateTimeField(auto_now=True)
    modo=models.CharField(choices=modoChoices,max_length=15, blank=True , null= True)
    cliente= models.ForeignKey(Cliente,verbose_name='cliente',on_delete= DO_NOTHING)
    estatus= models.CharField(choices=estatusChoices, default="Pendiente", max_length=15, blank=True , null= True)
    orden_compra= models.CharField(max_length=15, verbose_name='Orden de compra', blank=True , null= True)
    n_cotizacion= models.CharField(max_length=15,verbose_name='Cotización', blank=True , null= True)

    @property   
    def numero_entrada(self):
        list_Receptions= len(Recepcion.objects.all())
        list_reception_format = str(list_Receptions+1)
        n_entrada_format = list_reception_format.zfill(3)
        return n_entrada_format
    @numero_entrada.setter
    def numero_entrada(self, value):
        self.numero_entrada = value

    def save(self, *args,**kwargs):
        if not self.id:
            now = datetime.now() 
            self.n_entrada =  'IE' + '-' + (str(now.year)[2:]) + '-' +  str(self.numero_entrada)
            #self.fecha_de_recepcion = timezone.now()
        return super(Recepcion, self).save(*args, **kwargs)


    def __str__(self):
        return self.nombre
    
    def toJSON(self):
        item= model_to_dict(self)
        return item
    class Meta:
        verbose_name='Recepciones'
        verbose_name_plural='Recepciones'
        db_table='g_recepcion'
        ordering= ['n_entrada']

class Ingreso(models.Model):
    Calibracion = 'Calibración'
    Calificacion = 'Calificación'
    servChoices = [
        (Calibracion, 'Calibración'),
        (Calificacion, 'Calificación'),
    ]
    id= models.AutoField(primary_key=True)
    n_recepcion =models.ForeignKey(Recepcion, null=False, blank=False,verbose_name='Número de entrada', on_delete=DO_NOTHING)
    n_servicio = models.ForeignKey(Servicio,null=True,blank=True, on_delete=DO_NOTHING,verbose_name='Servicio')
    serv_prest = models.CharField(choices=servChoices, max_length=15,verbose_name='Servicio prestado')
    fecha_ingreso = models.DateField(verbose_name='Fecha de ingreso a almacén')

    def toJSON(self):
        item= model_to_dict(self)
        return item
    class Meta:
        verbose_name='Ingreso'
        verbose_name_plural='Ingresos'
        db_table='g_ingresos'
        ordering= ['id']