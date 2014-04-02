# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '0002_auto_20140226_1217'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Modulo',
        ),
    ]
