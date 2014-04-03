# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0006_auto_20140330_2220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina',
            name='foto',
            field=models.ForeignKey(blank=True, to_field='id', null=True, to='modulos.Imagen'),
        ),
    ]
