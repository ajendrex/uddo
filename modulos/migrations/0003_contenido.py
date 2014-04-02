# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0002_pagina'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contenido',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('pagina', models.ForeignKey(to='modulos.Pagina', to_field='id')),
                ('orden', models.IntegerField()),
                ('html', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
