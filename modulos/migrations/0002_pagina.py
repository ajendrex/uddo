# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pagina',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('modulo', models.ForeignKey(to='modulos.Modulo', to_field='id')),
                ('nombre_archivo', models.CharField(max_length=30)),
                ('titulo', models.CharField(max_length=200)),
                ('foto', models.ForeignKey(to='modulos.Imagen', to_field='id')),
                ('orden', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
