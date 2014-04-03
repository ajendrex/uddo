# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_auto_20140329_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pagina',
            name='foto',
            field=models.ForeignKey(to='modulos.Imagen', null=True, to_field='id'),
        ),
    ]
