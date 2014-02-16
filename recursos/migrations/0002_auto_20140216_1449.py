# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='versionrecurso',
            name='aprobado_di',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='versionrecurso',
            name='aprobado_coordinador',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='versionrecurso',
            name='aprobado_profesor',
            field=models.BooleanField(default=False),
            preserve_default=False,
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='aprobado_profesor',
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='aprobado_coordinador',
        ),
        migrations.RemoveField(
            model_name='recurso',
            name='aprobado_di',
        ),
    ]
