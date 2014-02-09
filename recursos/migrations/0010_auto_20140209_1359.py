# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0009_auto_20140209_0905'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FechaEntrega',
        ),
        migrations.AlterField(
            model_name='recurso',
            name='entrega_estimada',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
