# encoding: utf8
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recursos', '0006_auto_20140206_2242'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comentariorecurso',
            name='fec_comentario',
        ),
    ]
