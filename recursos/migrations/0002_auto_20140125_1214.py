# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recursos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComentarioRecurso',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('owner', models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id')),
                ('recurso', models.ForeignKey(to='recursos.Recurso', to_field='id')),
                ('comentario', models.TextField()),
                ('fec_comentario', models.DateTimeField()),
                ('fec_creacion', models.DateTimeField(auto_now_add=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='descripcion',
            field=models.CharField(max_length=5000, null=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='curso',
            field=models.ForeignKey(to='cursos.Curso', to_field='id', null=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='costoFinal',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='costo',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='link',
            field=models.CharField(max_length=300, null=True),
        ),
    ]
