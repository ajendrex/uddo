# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0003_auto_20140226_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='insumorecurso',
            name='archivo',
            field=models.FileField(upload_to='insumos/%Y/%m/%d/', max_length=255),
        ),
        migrations.AlterField(
            model_name='versionrecurso',
            name='archivo',
            field=models.FileField(upload_to='versiones/%Y/%m/%d/', max_length=255),
        ),
    ]
