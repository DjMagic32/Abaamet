# Generated by Django 4.0 on 2022-01-05 05:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cargo',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('nombre', models.CharField(max_length=100, verbose_name='cargo')),
            ],
            options={
                'verbose_name': 'Cargo',
                'verbose_name_plural': 'Cargos',
                'db_table': 'g_cargo',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=40, null=True, verbose_name='nombre_completo')),
                ('telefono', models.CharField(max_length=12, verbose_name='telefono')),
                ('telefono_ad', models.CharField(max_length=12, null=True, verbose_name='telefono_ad')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
            ],
        ),
        migrations.CreateModel(
            name='Cotizaciones',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False)),
                ('fecha_ini', models.DateField()),
                ('fecha_fin', models.DateField()),
                ('comentario', models.CharField(max_length=254)),
                ('subtotal', models.FloatField()),
                ('viaticos', models.FloatField()),
                ('descuento', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('total_sin_iva', models.FloatField()),
                ('is_cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Direccion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('num_interior', models.CharField(max_length=80, null=True, verbose_name='num_interior')),
                ('num_exterior', models.CharField(max_length=80, null=True, verbose_name='num_exterior')),
                ('calle', models.CharField(max_length=50, null=True, verbose_name='calle')),
                ('colonia', models.CharField(max_length=20, null=True, verbose_name='colonia')),
                ('pais', models.CharField(max_length=15, verbose_name='pais')),
                ('referencia', models.CharField(max_length=254, null=True, verbose_name='referencia')),
                ('localidad', models.CharField(max_length=30, null=True, verbose_name='localidad')),
                ('estado', models.CharField(max_length=20, null=True, verbose_name='estado')),
                ('municipio', models.CharField(max_length=20, null=True, verbose_name='municipio')),
                ('codigo_postal', models.PositiveIntegerField(verbose_name='codigo_postal')),
            ],
        ),
        migrations.CreateModel(
            name='Empresa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_empresa', models.CharField(blank=True, max_length=150, null=True, verbose_name='Nombre de empresa')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email')),
                ('nombre', models.CharField(blank=True, max_length=100, null=True, verbose_name='Nombre')),
                ('phone', models.CharField(max_length=12, null=True, verbose_name='phone')),
                ('razon_social', models.CharField(max_length=50, verbose_name='razon_social')),
                ('numero_cliente', models.CharField(max_length=50, verbose_name='Numero de Cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('precio', models.PositiveIntegerField(verbose_name='precio')),
                ('detalle', models.TextField(verbose_name='detalle')),
                ('activo', models.BooleanField(default=True, verbose_name='activo')),
            ],
            options={
                'verbose_name': 'Servicio',
                'verbose_name_plural': 'Servicios',
                'db_table': 'g_servicio',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('email', models.EmailField(max_length=254, verbose_name='email')),
                ('cargo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='general.cargo', verbose_name='cargo')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'db_table': 'g_usuarios',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Sucursal',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre_sucursal', models.CharField(max_length=50, null=True, verbose_name='Sucursal')),
                ('rfc', models.CharField(max_length=30, null=True, verbose_name='rfc')),
                ('id_direccion', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general.direccion', verbose_name='direccion')),
                ('id_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general.empresa', verbose_name='empresa')),
            ],
        ),
        migrations.CreateModel(
            name='Serv_Cot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_cotizacion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.cotizaciones')),
                ('id_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='general.servicio')),
            ],
        ),
        migrations.CreateModel(
            name='Recepcion',
            fields=[
                ('n_entrada', models.AutoField(primary_key=True, serialize=False, verbose_name='n_entrada')),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('marca', models.CharField(max_length=50, verbose_name='marca')),
                ('modelo', models.CharField(max_length=50, verbose_name='model')),
                ('serie', models.CharField(max_length=15, verbose_name='detalle')),
                ('identificacion', models.CharField(max_length=10, verbose_name='identificacion')),
                ('descripcion_particular', models.CharField(max_length=25, verbose_name='descripcion_particular')),
                ('fecha_de_recepcion', models.DateField(null=True, verbose_name='fecha_de_recepcion')),
                ('modo', models.CharField(choices=[('Paqueteria', 'Paqueteria'), ('Abaa Recogio', 'AbaaRecogio'), ('Cliente Entrego', 'ClienteEntrego')], max_length=15)),
                ('estatus', models.CharField(choices=[('Devuelto', 'Devuelto'), ('Pendiente', 'Pendiente'), ('Aprobado', 'Aprobado')], max_length=15)),
                ('orden_compra', models.CharField(max_length=15, verbose_name='orden_ compra')),
                ('n_cotizacion', models.CharField(max_length=15, verbose_name='cotizacion')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='general.cliente', verbose_name='cliente')),
            ],
            options={
                'verbose_name': 'Recepciones',
                'verbose_name_plural': 'Recepciones',
                'db_table': 'g_recepcion',
                'ordering': ['n_entrada'],
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50, verbose_name='nombre')),
                ('precio', models.PositiveIntegerField(verbose_name='precio')),
                ('marca', models.CharField(max_length=50, verbose_name='marca')),
                ('modelo', models.CharField(max_length=50, verbose_name='model')),
                ('detalle', models.TextField(verbose_name='detalle')),
                ('activo', models.BooleanField(default=True, verbose_name='activo')),
                ('id_empresa', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general.empresa', verbose_name='empresa')),
            ],
            options={
                'verbose_name': 'Producto',
                'verbose_name_plural': 'Productos',
                'db_table': 'g_producto',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('serv_prest', models.CharField(choices=[('Calibracion', 'Calibracion'), ('Calificacion', 'Calificacion')], max_length=15, verbose_name='serv_prest')),
                ('fecha_ingreso', models.DateField(verbose_name='fecha_almacen')),
                ('n_recepcion', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='general.recepcion', verbose_name='n_entrada')),
                ('n_servicio', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general.servicio', verbose_name='servicio')),
            ],
            options={
                'verbose_name': 'Ingreso',
                'verbose_name_plural': 'Ingresos',
                'db_table': 'g_ingresos',
                'ordering': ['id'],
            },
        ),
        migrations.AddField(
            model_name='cliente',
            name='id_empresa',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general.empresa', verbose_name='empresa'),
        ),
        migrations.AddField(
            model_name='cliente',
            name='sucursal_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='general.sucursal', verbose_name='empresa'),
        ),
    ]
