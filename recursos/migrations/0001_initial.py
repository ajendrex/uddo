# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('nombre', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(to_field='id', null=True, to='cursos.Curso')),
                ('creador', models.ForeignKey(to_field='id', to=settings.AUTH_USER_MODEL)),
                ('tipo', models.CharField(max_length=3, choices=[('INT', 'Interactivo'), ('REC', 'Recreación'), ('ANI', 'Animación'), ('ENT', 'Entrevista'), ('DIG', 'Digitalización'), ('DIA', 'Diagramación'), ('GRA', 'Gráfica'), ('FOT', 'Fotografía'), ('EST', 'Estilaje')])),
                ('categoria', models.CharField(max_length=1, choices=[('B', 'Básico'), ('M', 'Medio'), ('F', 'Full'), ('E', 'Especial')])),
                ('proveedor', models.ForeignKey(to_field='id', null=True, to=settings.AUTH_USER_MODEL, blank=True)),
                ('costo', models.IntegerField(null=True, blank=True)),
                ('costoFinal', models.IntegerField(null=True, blank=True)),
                ('descripcion', models.TextField(blank=True)),
                ('link', models.CharField(max_length=300, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('entrega_estimada', models.DateTimeField(null=True, blank=True)),
                ('total_versiones', models.IntegerField(default=0)),
                ('aprobado_di', models.BooleanField(default=False)),
                ('aprobado_profesor', models.BooleanField(default=False)),
                ('aprobado_coordinador', models.BooleanField(default=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComentarioRecurso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('autor', models.ForeignKey(to_field='id', null=True, to=settings.AUTH_USER_MODEL)),
                ('recurso', models.ForeignKey(to_field='id', to='recursos.Recurso')),
                ('comentario', models.TextField()),
                ('fec_creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InsumoRecurso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('archivo', models.FileField(upload_to='insumos/%Y/%m/%d/')),
                ('recurso', models.ForeignKey(to_field='id', to='recursos.Recurso')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('tag', models.CharField(unique=True, max_length=100)),
                ('recursos', models.ManyToManyField(to='recursos.Recurso')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VersionRecurso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('archivo', models.FileField(upload_to='versiones/%Y/%m/%d/')),
                ('fecha_entrega', models.DateTimeField(auto_now_add=True)),
                ('recurso', models.ForeignKey(to_field='id', to='recursos.Recurso')),
                ('version', models.IntegerField()),
                ('proveedor', models.ForeignKey(to_field='id', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComentarioVersionRecurso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('autor', models.ForeignKey(to_field='id', null=True, to=settings.AUTH_USER_MODEL)),
                ('version', models.ForeignKey(to_field='id', to='recursos.VersionRecurso')),
                ('comentario', models.TextField()),
                ('fec_creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
