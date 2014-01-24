# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('cursos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tag', models.CharField(unique=True, max_length=100)),
                ('recursos', models.ManyToManyField(to='recursos.Recurso')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('curso', models.ForeignKey(to='cursos.Curso', to_field='id')),
                ('creador', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('tipo', models.CharField(max_length=3, choices=(('INT', 'Interactivo'), ('REC', 'RecreaciÃ³n'), ('ANI', 'AnimaciÃ³n'), ('ENT', 'Entrevista'), ('DIG', 'DigitalizaciÃ³n'), ('DIA', 'DiagramaciÃ³n'), ('GRA', 'GrÃ¡fica'), ('FOT', 'FotografÃ\xada'), ('EST', 'Estilaje')))),
                ('categoria', models.CharField(max_length=1, choices=(('B', 'BÃ¡sico'), ('M', 'Medio'), ('F', 'Full'), ('E', 'Especial')))),
                ('proveedor', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', null=True)),
                ('costo', models.IntegerField()),
                ('costoFinal', models.IntegerField()),
                ('descripcion', models.CharField(max_length=5000)),
                ('link', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FechaEntrega',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateTimeField()),
                ('recurso', models.ForeignKey(to='recursos.Recurso', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InsumoRecurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to='insumos/%Y/%m/%d/')),
                ('recurso', models.ForeignKey(to='recursos.Recurso', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='VersionRecurso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('archivo', models.FileField(upload_to='versiones/%Y/%m/%d/')),
                ('recurso', models.ForeignKey(to='recursos.Recurso', to_field='id')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
