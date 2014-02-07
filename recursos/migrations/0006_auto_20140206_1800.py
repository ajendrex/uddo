# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('recursos', '0005_auto_20140130_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='categoria',
            field=models.CharField(max_length=1, choices=(('B', 'Básico'), ('M', 'Medio'), ('F', 'Full'), ('E', 'Especial'))),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='tipo',
            field=models.CharField(max_length=3, choices=(('INT', 'Interactivo'), ('REC', 'Recreación'), ('ANI', 'Animación'), ('ENT', 'Entrevista'), ('DIG', 'Digitalización'), ('DIA', 'Diagramación'), ('GRA', 'Gráfica'), ('FOT', 'Fotografía'), ('EST', 'Estilaje'))),
        ),
    ]
