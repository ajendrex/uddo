# encoding: utf8
from django.db import models, migrations
from datetime import date


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0008_auto_20140209_0742'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='entrega_estimada',
            field=models.DateTimeField(null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='versionrecurso',
            name='fecha_entrega',
            field=models.DateTimeField(default=date(2014, 2, 9), auto_now_add=True),
            preserve_default=False,
        ),
    ]
