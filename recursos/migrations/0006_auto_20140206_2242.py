# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('recursos', '0005_auto_20140130_2238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='tipo',
            field=models.CharField(choices=[('INT', 'Interactivo'), ('REC', 'Recreación'), ('ANI', 'Animación'), ('ENT', 'Entrevista'), ('DIG', 'Digitalización'), ('DIA', 'Diagramación'), ('GRA', 'Gráfica'), ('FOT', 'Fotografía'), ('EST', 'Estilaje')], max_length=3),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='descripcion',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='categoria',
            field=models.CharField(choices=[('B', 'Básico'), ('M', 'Medio'), ('F', 'Full'), ('E', 'Especial')], max_length=1),
        ),
    ]
