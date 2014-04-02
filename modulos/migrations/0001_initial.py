# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cursos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('nombre', models.CharField(max_length=20)),
                ('archivo', models.FileField(upload_to='img/', max_length=255)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Modulo',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('curso', models.ForeignKey(to='cursos.Curso', to_field='id')),
                ('nombre_corto', models.CharField(max_length=20)),
                ('nombre_largo', models.CharField(max_length=200)),
                ('orden', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
