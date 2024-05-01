# Generated by Django 5.0.4 on 2024-05-01 11:10

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('medico', '0001_initial'),
        ('paciente', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='datasabertas',
            name='consultas',
            field=models.ManyToManyField(related_name='datas_abertas', to='paciente.consulta'),
        ),
        migrations.AddField(
            model_name='datasabertas',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='dadosmedico',
            name='especialidade',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='medico.especialidades'),
        ),
    ]
