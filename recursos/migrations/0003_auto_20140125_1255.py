# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):
    
    dependencies = [
        ('recursos', '0002_auto_20140125_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recurso',
            name='descripcion',
            field=models.CharField(max_length=5000),
        ),
        migrations.AlterField(
            model_name='recurso',
            name='link',
            field=models.CharField(max_length=300),
        ),
    ]
