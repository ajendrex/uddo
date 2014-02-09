# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0007_remove_comentariorecurso_fec_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='recurso',
            name='aprobado_coordinador',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recurso',
            name='aprobado_profesor',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recurso',
            name='aprobado_di',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
