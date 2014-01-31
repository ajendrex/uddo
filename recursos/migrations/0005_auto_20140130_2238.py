# encoding: utf8
from django.db import models, migrations
from datetime import date
from django.conf import settings


class Migration(migrations.Migration):
    
    dependencies = [
        ('recursos', '0004_auto_20140125_1305'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='fecha_creacion',
            field=models.DateTimeField(auto_now_add=True, default=date(2014, 1, 30)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentariorecurso',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, to_field='id', null=True),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='descripcion',
            field=models.CharField(blank=True, max_length=5000),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='link',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
