# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '__first__'),
        ('modulos', '0003_contenido'),
    ]

    operations = [
        migrations.CreateModel(
            name='RecAprendizaje',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True, serialize=False)),
                ('modulo', models.ForeignKey(to='modulos.Modulo', to_field='id')),
                ('categoria', models.CharField(max_length=3, choices=[('TAR', 'Para realizar la Tarea'), ('OBL', 'Obligatorios'), ('OPC', 'Opcionales'), ('BIB', 'Bibliografía'), ('MED', 'Muldimedia')])),
                ('recurso', models.ForeignKey(to='recursos.Recurso', to_field='id')),
                ('leyenda', models.CharField(max_length=300)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
