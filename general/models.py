from django.db import models
from django.db.models.deletion import DO_NOTHING
from django.forms.models import model_to_dict
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Direccion(models.Model):
    id = models.AutoField(primary_key=True)
    num_interior= models.IntegerField(null=True,verbose_name='num_interior')
    num_exterior= models.IntegerField(null=True,verbose_name='num_exterior')
    calle= models.CharField(null=True, max_length=50,verbose_name='calle')
    colonia= models.CharField(null=True, max_length=20,verbose_name='colonia')
    pais= models.CharField(null=False,max_length=15,verbose_name='pais')
    referencia= models.CharField(max_length=254, null=True,verbose_name='referencia')
    localidad= models.CharField(max_length=30,null=True,verbose_name='localidad')
    estado= models.CharField(max_length=20,null=True,verbose_name='estado')
    municipio= models.CharField(max_length=20, null=True,verbose_name='municipio')
    codigo_postal= models.PositiveIntegerField(null=False,verbose_name='codigo_postal')
    def __str__(self):
        return self.localidad
    def toJSON(self):
        item= model_to_dict(self)
        return item

class Empresa(models.Model):
    id = models.AutoField(primary_key=True)
    razon_social = models.CharField(max_length=50,verbose_name='razon_social')
    def __str__(self):
        return self.razon_social
    def toJSON(self):
        item= model_to_dict(self)
        return item


class Sucursal(models.Model):
    id= models.AutoField(primary_key=True)
    rfc = models.CharField(null=True, max_length=30,verbose_name='rfc')
    id_direccion= models.ForeignKey(Direccion,null=True, blank=True, on_delete= DO_NOTHING,verbose_name='direccion')
    id_empresa = models.ForeignKey(Empresa,null=True, blank=True, on_delete=DO_NOTHING,verbose_name='empresa')
    def __str__(self):
        return self.rfc
    def toJSON(self):
        item= model_to_dict(self)
        return item


class Cliente(models.Model):
    id = models.AutoField(primary_key=True)
    nombre_completo = models.CharField(null=True,max_length=40,verbose_name='nombre_completo')
    telefono = models.CharField(max_length=12,verbose_name='telefono')
    telefono_ad = models.CharField(max_length=12,null=True,verbose_name='telefono_ad')
    email= models.EmailField(max_length=254,verbose_name='email')
    id_sucursal= models.ForeignKey(Sucursal,null=True, blank=True, on_delete=DO_NOTHING,verbose_name='id_sucursal')
    def __str__(self):
        return self.nombre_completo
    def toJSON(self):
        item= model_to_dict(self)
        return item
    
class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50,verbose_name='nombre')
    precio = models.PositiveIntegerField(verbose_name='precio')
    marca = models.CharField(max_length=50,verbose_name='marca')
    modelo = models.CharField(max_length=50,verbose_name='model')
    detalle = models.TextField( verbose_name='detalle')
    activo= models.BooleanField(verbose_name='activo', default=True)
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
    nombre = models.CharField(max_length=50,verbose_name='nombre')
    precio = models.PositiveIntegerField(verbose_name='precio')
    detalle = models.TextField( verbose_name='detalle')
    activo= models.BooleanField(verbose_name='activo', default=True)
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
    nombre=models.CharField(max_length=100, verbose_name='cargo')
    def __str__(self):
        return self.nombre
    class Meta:
        verbose_name='Cargo'
        verbose_name_plural='Cargos'
        db_table='g_cargo'
        ordering=['id']

class Usuario(models.Model):
    id= models.PositiveIntegerField(primary_key=True, verbose_name='id')
    email= models.EmailField(verbose_name='email')
    cargo= models.ForeignKey(Cargo,null=False, blank=False,on_delete=DO_NOTHING, verbose_name='cargo')
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
    

    n_entrada = models.AutoField(primary_key=True,verbose_name='n_entrada')
    nombre = models.CharField(max_length=50,verbose_name='nombre')
    marca = models.CharField(max_length=50,verbose_name='marca')
    modelo = models.CharField(max_length=50,verbose_name='model')
    serie = models.CharField( verbose_name='detalle',max_length=15)
    identificacion= models.CharField(verbose_name='identificacion',max_length=10)
    descripcion_particular = models.CharField(verbose_name='descripcion_particular',max_length=25)
    fecha_de_recepcion = models.DateField(verbose_name='fecha_de_recepcion',null=True)
    modo=models.CharField(choices=modoChoices,max_length=15)
    cliente= models.ForeignKey(Cliente,verbose_name='cliente',on_delete= DO_NOTHING)
    estatus= models.CharField(choices=estatusChoices, max_length=15)
    orden_compra= models.CharField(max_length=15, verbose_name='orden_ compra')
    n_cotizacion= models.CharField(max_length=15,verbose_name='cotizacion')
    

    def save(self, *args,**kwargs):
        self.fecha_de_recepcion = timezone.now()
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
    Calibracion = 'Calibracion'
    Calificacion = 'Calificacion'
    servChoices = [
        (Calibracion, 'Calibracion'),
        (Calificacion, 'Calificacion'),
    ]
    id= models.AutoField(primary_key=True)
    n_recepcion =models.ForeignKey(Recepcion, null=False, blank=False,verbose_name='n_entrada', on_delete=DO_NOTHING)
    n_servicio = models.ForeignKey(Servicio,null=True,blank=True, on_delete=DO_NOTHING,verbose_name='servicio')
    serv_prest = models.CharField(choices=servChoices, max_length=15,verbose_name='serv_prest')
    fecha_ingreso = models.DateField(verbose_name='fecha_almacen')

    def toJSON(self):
        item= model_to_dict(self)
        return item
    class Meta:
        verbose_name='Ingreso'
        verbose_name_plural='Ingresos'
        db_table='g_ingresos'
        ordering= ['id']
