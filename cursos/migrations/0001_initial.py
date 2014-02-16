# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('owner', models.ForeignKey(to_field='id', to=settings.AUTH_USER_MODEL)),
                ('profesor', models.ForeignKey(to_field='id', null=True, to=settings.AUTH_USER_MODEL)),
                ('codigo', models.CharField(max_length=20)),
                ('nombre', models.CharField(max_length=200)),
                ('fec_creacion', models.DateTimeField(auto_now_add=True)),
                ('fec_modificacion', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='ComentarioCurso',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('owner', models.ForeignKey(to_field='id', to=settings.AUTH_USER_MODEL)),
                ('curso', models.ForeignKey(to_field='id', to='cursos.Curso')),
                ('estado', models.CharField(max_length=2, choices=[('NI', 'No Iniciado'), ('DC', 'DiseÃ±o Conceptual'), ('DT', 'DiseÃ±o Detallado'), ('DR', 'DiseÃ±o de Recursos'), ('IM', 'ImplantaciÃ³n'), ('RV', 'RevisiÃ³n'), ('EN', 'Entregado')])),
                ('comentario', models.TextField()),
                ('fec_creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('curso', models.ForeignKey(to_field='id', to='cursos.Curso')),
                ('orden', models.IntegerField()),
                ('titulo', models.CharField(max_length=200)),
                ('nombreCorto', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
