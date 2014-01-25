# encoding: utf8
from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):
    
    dependencies = [
        ('recursos', '0003_auto_20140125_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='costo',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='costoFinal',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='proveedor',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', null=True, blank=True),
        ),
    ]
