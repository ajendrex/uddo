# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0004_recaprendizaje'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recaprendizaje',
            name='id',
        ),
        migrations.AlterField(
            model_name='recaprendizaje',
            name='modulo',
            field=models.OneToOneField(to='modulos.Modulo', primary_key=True, serialize=False, to_field='id'),
        ),
    ]
