# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0002_auto_20140216_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='versionrecurso',
            name='aprobado_di',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='versionrecurso',
            name='aprobado_profesor',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='versionrecurso',
            name='aprobado_coordinador',
            field=models.BooleanField(default=False),
        ),
    ]
